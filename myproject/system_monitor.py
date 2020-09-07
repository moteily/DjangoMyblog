#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pymysql
import gevent
import time
import psutil
import pynvml

# 解决wind10错误OSError: raw write() returned invalid length
import win_unicode_console
pymysql.install_as_MySQLdb()
win_unicode_console.enable()


class MyPyMysql:
    def __init__(self, host, port, username, password, db, charset='utf8'):
        self.host = host  # mysql主机地址
        self.port = port  # mysql端口
        self.username = username  # mysql远程连接用户名
        self.password = password  # mysql远程连接密码
        self.db = db  # mysql使用的数据库名
        self.charset = charset  # mysql使用的字符编码,默认为utf8
        self.pymysql_connect()  # __init__初始化之后，执行的函数

    def pymysql_connect(self):
        # pymysql连接mysql数据库
        # 需要的参数host,port,user,password,db,charset
        self.conn = pymysql.connect(host=self.host,  # 这里加上self表示为对象的属性 不加只能表示函数内的属性 不能被类内其他函数调用
                                    port=self.port,
                                    user=self.username,
                                    password=self.password,
                                    db=self.db,
                                    charset=self.charset
                                    )
        # 连接mysql后执行的函数
        self.asynchronous()

    def getCPUstate(self, interval=1):
        cur_cpu = psutil.cpu_percent(interval)  # CPU使用量
        cpu_cores = psutil.cpu_count(logical=True)  # CPU总核心数
        line = {
            'cur_cpu': cur_cpu,
            'cpu_cores': cpu_cores,
        }
        return line

    def getMemorystate(self):
        phymem = psutil.virtual_memory()
        cur_mem = phymem.percent
        mem_use = int(phymem.used / 1024 / 1024)
        mem_all = int(phymem.total / 1024 / 1024)

        line = {
            'mem_use': mem_use,
            'mem_all': mem_all,
            'cur_mem': cur_mem,
        }
        return line

    def GetGPUstate(self):
        pynvml.nvmlInit()
        gpudriver_info = pynvml.nvmlSystemGetDriverVersion()  # 获取驱动信息
        gpu_count = pynvml.nvmlDeviceGetCount()  # 显卡数量
        handle = pynvml.nvmlDeviceGetHandleByIndex(0)  # 这里的0是GPU id
        gpu_name = pynvml.nvmlDeviceGetName(handle)  # 显卡型号
        meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)
        line = {
            'gpudriver_info': gpudriver_info,
            'gpu_count':  gpu_count,  # 显卡数量
            'gpu_name': gpu_name,   # 显卡型号
            'gpumem_all': int(meminfo.total/1024/1024),  # 总显存大小
            'gpumem_use': int(meminfo.used/1024/1024),  # 已用显存
            'gpumem_free': int(meminfo.free/1024/1024),  # 剩余显存
            'cur_gpu':  float(meminfo.used/meminfo.total)   # 显存使用率
        }
        return line

    def run(self):
        # 创建游标
        self.cur = self.conn.cursor()
        # 定义sql语句
        sql = "insert into DataShow_system_monitor  (cpu_cores,cur_cpu,mem_use,mem_all,cur_mem,\
            gpu_count,gpu_name,gpudriver_info,gpumem_all,gpumem_use,gpumem_free,cur_gpu,\
            create_time,time_stamp) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        print(sql)

        # 定义数据
        cpu = self.getCPUstate()  # cpu info信息
        mem = self.getMemorystate()  # 内存info信息
        gpu = self.GetGPUstate()    # gpu info信息
        cur_cpu = cpu['cur_cpu']  # CPU使用率
        cpu_cores = cpu['cpu_cores']  # CPU核数
        mem_use = mem['mem_use']  # 当前使用内存
        mem_all = mem['mem_all']  # 总内存
        cur_mem = mem['cur_mem']  # 内存使用率
        gpu_count = gpu['gpu_count']  # 显卡数量
        gpu_name = gpu['gpu_name']  # 显卡型号
        gpudriver_info = gpu['gpudriver_info']  # 显卡驱动信息
        gpumem_all = gpu['gpumem_all']  # 总显存大小
        gpumem_use = gpu['gpumem_use']  # 已用显存
        gpumem_free = gpu['gpumem_free']   # 剩余显存
        cur_gpu = gpu['cur_gpu']   # 显存使用率
        struct_time = time.localtime()
        create_time = time.strftime(
            "%Y-%m-%d %H:%M:%S", struct_time)  # 转换为标准时间
        t = time.time()  # 当前时间戳
        time_stamp = int(round(t * 1000))  # 转换为毫秒的时间戳

        print((cpu_cores, cur_cpu, mem_use, mem_all, cur_mem,
               gpu_count, gpu_name, gpudriver_info, gpumem_all, gpumem_use, gpumem_free, cur_gpu, create_time, time_stamp))

        # 执行插入一行数据，如果插入多行，使用executemany(sql语句,数据(需一个元组类型))
        content = self.cur.execute(
            sql, (cpu_cores, cur_cpu, mem_use, mem_all, cur_mem,
                  gpu_count, gpu_name, gpudriver_info, gpumem_all, gpumem_use, gpumem_free, cur_gpu, create_time, time_stamp))
        if content:
            print('插入ok')

        # 提交数据,必须提交，不然数据不会保存
        self.conn.commit()

    def asynchronous(self):
        # 执行30次协程任务
        for i in range(0, 30):
            time.sleep(4)  # 等待10秒
            gevent.spawn(self.run())  # 执行方法

        self.cur.close()  # 关闭游标
        self.conn.close()  # 关闭pymysql连接


if __name__ == '__main__':
    start_time = time.time()  # 计算程序开始时间
    st = MyPyMysql('47.98.149.64', 3306, 'root', '460716687',
                   'DjangoMyblog')  # 实例化类，传入必要参数
    print('程序耗时{:.2f}'.format(time.time() - start_time))  # 计算程序总耗时
