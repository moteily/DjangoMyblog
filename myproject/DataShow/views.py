from django.shortcuts import render
from .models import CPUState
from .models import system_monitor
from django.http import HttpResponse
from django.http.response import JsonResponse
import json
# Create your views here.


def chart_json(request):
    # Django不支持负切片，采用下面的方式获取最新的20条数据
    monitor = system_monitor.objects.latest('id')
    # length = system_monit.count()  # 获取表数据总长度
    # system_monit = system_monit[length-20:length]
    print(request.POST)
    data = []  # 创建一个空列表
    TimeStamp = int(monitor.time_stamp)
    cur_cpu = float('%.2f' % monitor.cur_cpu)
    mem_use = int(monitor.mem_use)  # 当前使用内存
    mem_all = int(monitor.mem_all)  # 总内存
    cur_mem = float('%.2f' % monitor.cur_mem)  # 内存使用率
    cur_gpu = float('%.2f' % monitor.cur_gpu)
    gpumem_use = int(monitor.gpumem_use)
    gpumem_free = int(monitor.gpumem_free)
    # cpu_cores = int(system_monit.cpu_cores)
    data.append({'time': TimeStamp, 'cur_cpu': cur_cpu,
                 'cur_mem': cur_mem, 'mem_use': mem_use, 'mem_all': mem_all,
                 'cur_gpu': cur_gpu, 'gpumem_use': gpumem_use, 'gpumem_free': gpumem_free})
    # for i in system_monit:  # 遍历，拼横纵坐标
    #     # 横坐标为时间戳,纵坐标为cpu使用率。注意，必须转换类型，否则数据不对。
    #     TimeStamp = int(i.time_stamp)
    #     cur_cpu = float('%.2f' % i.cur_cpu)
    #     data.append({'time': TimeStamp, 'cur_cpu': cur_cpu})
    # print(data)
    # isdict = json.dumps(data)  # json序列化列表
    # return HttpResponse(isdict, content_type="application/json")  # 执行类型为json
    response = JsonResponse(data, safe=False)
    return response


def system_monit(request):
    monitor = system_monitor.objects.latest('id')
    cpu_cores = int(monitor.cpu_cores)
    mem_all = int(monitor.mem_all)  # 总内存
    return render(request, "DataShow/sys_monitor.html", {"cpu_cores": cpu_cores, "mem_all": mem_all})


def gpu_monit(request):
    monitor = system_monitor.objects.latest('id')
    gpu_count = int(monitor.gpu_count)
    gpumem_all = int(monitor.gpumem_all)  # 总显存
    gpu_name = monitor.gpu_name
    gpudriver_info = monitor.gpudriver_info
    gpumem_free = monitor.gpumem_free
    gpumem_use = monitor.gpumem_use
    cur_gpu = monitor.cur_gpu
    return render(request, "DataShow/gpu_monitor.html",
                  {"gpu_count": gpu_count, "gpumem_all": gpumem_all, 'gpu_name': gpu_name, 'gpudriver_info': gpudriver_info,
                   "gpumem_free": gpumem_free, "gpumem_use": gpumem_use, "cur_gpu": cur_gpu})


def cpu_state(request):
    return render(request, "DataShow/cpu_state.html")
