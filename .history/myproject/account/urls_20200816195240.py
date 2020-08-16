from django.urls import path
from . import views
from django.contrib.auth import  views as auth_views

urlpatterns = [
    # path('login/', views.user_login, name='user_login'),  #使用自己写的登录视图
    path('login/', auth_views.LoginView.as_view(template_name='account/login2.html'), name='user_login'), #使用Django内置的登录视图
    path('logout/', auth_views.LogoutView.as_view(), name='user_logout'),  #name参数的作用为 html文件中填写超链接标签可以用name来代替具体的域名,此句调用Django内置的管理员登出
    path('logout/', auth_views.LogoutView.as_view(template_name=a), name='user_logout'),
]
