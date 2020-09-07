from django.db import models
# import GetData #自定义获取系统数据的库函数  
# Create your models here.


class CPUState(models.Model):
    # 字符串类型，必须要给出max_length,对应于html中的<input type="text">
    # state = GetData.GetCPUstate()
    number = models.CharField(max_length = 100)
    cores = models.CharField(max_length = 100)
    use_rate = models.CharField(max_length = 300)
    def __str__(self): 
        return self.number

class system_monit_cpu(models.Model):
    id = models.BigAutoField(primary_key=True)
    #类型为decimal(10,2)，长度为10，小数点保留2位
    cpu_cores = models.IntegerField()
    cur_cpu = models.DecimalField(max_digits=10, decimal_places=2)
    #类型为int(11)，11是默认长度
    cur_mem = models.IntegerField()
    mem_rate = models.DecimalField(max_digits=10, decimal_places=2)
    mem_all = models.IntegerField()
    #类型为datetime
    create_time = models.DateTimeField()
    #由于毫秒的时间戳超过了timestamp的长度，所以只能设置bigint了。
    time_stamp = models.BigIntegerField()


class system_monitor(models.Model):
    id = models.BigAutoField(primary_key=True)
    #类型为decimal(10,2)，长度为10，小数点保留2位
    cpu_cores = models.IntegerField()
    cur_cpu = models.DecimalField(max_digits=10, decimal_places=2)
    #以下为内存信息
    mem_use = models.IntegerField()
    mem_all = models.IntegerField()
    cur_mem = models.DecimalField(max_digits=10, decimal_places=2)
    #以下为显卡信息
    gpu_count = models.IntegerField()
    gpu_name = models.CharField(max_length=100)
    gpudriver_info = models.CharField(max_length=100)
    gpumem_all = models.IntegerField()
    gpumem_use = models.IntegerField()
    gpumem_free = models.IntegerField()
    cur_gpu = models.DecimalField(max_digits=10, decimal_places=2)
    #类型为datetime
    create_time = models.DateTimeField()
    #由于毫秒的时间戳超过了timestamp的长度，所以只能设置bigint了。
    time_stamp = models.BigIntegerField()
