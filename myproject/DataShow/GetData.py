# -*- coding: utf-8 -*-
# pip install nvidia-ml-py3
import os
import time
import psutil
import sys
import pynvml
import socket
import pymysql
pymysql.install_as_MySQLdb()


hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)


def GetCPUstate(time_count=2):  # 返回CPU个数 总核数以及每个核的使用率
    CPUstate = {"Number": str(psutil.cpu_count(logical=False)),
                "Cores": str(psutil.cpu_count(logical=True)),
                "UseRate": str(psutil.cpu_percent(time_count, 0))}
    return CPUstate
def GetGPUstate():
    pynvml.nvmlInit()
    handle = pynvml.nvmlDeviceGetHandleByIndex(0)  # 这里的0是GPU id
    meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)
    GPUstate = {
        "Number": str(pynvml.nvmlDeviceGetCount()), # 显卡数量
        "TotalSize": str(meminfo.total/1024),  # 第二块显卡总的显存大小
        "UsedSize": str(meminfo.used/1024),
        "FreeSize": str(meminfo.free/1024),
    }
    return GPUstate
print(GetCPUstate())
print(GetGPUstate())
# 监控网卡及流量状态
print(ip)
print(hostname)
# 监控cpu内存以及硬盘相关状态

db = pymysql.connect("47.98.149.64", "root", "460716687","DjangoMyblog",charset='utf8')
cursor = db.cursor()
sql = """INSERT INTO DataShow_cpustate(number,cores, use_rate)VALUES (%s,%s,%s)"""
CPUState = GetCPUstate()
row = cursor.execute(sql,(CPUState['Number'],CPUState['Cores'],CPUState['UseRate']))
db.commit()
cursor.close()
db.close()
