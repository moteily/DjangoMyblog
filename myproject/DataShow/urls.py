from django.urls import path
from . import views

urlpatterns = [
    # 第一个参数为空，表示访问根，因为在blog应用中，所以访问blog应用的根，即https://127.0.0.1:8080/blog/
    path('', views.system_monit, name='system_monit'),
    path('gpumonitor', views.gpu_monit, name='gpu_monit'),
    path('cpustate', views.cpu_state, name='cpu_state'),
    path('chartjson', views.chart_json, name='chart_json'),
    # 通过正则表达式确定views.blog_article为要访问的视图
]
