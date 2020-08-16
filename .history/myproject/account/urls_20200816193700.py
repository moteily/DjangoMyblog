from django.urls import path
from . import views
from django.contrib.auth import  views as auth_views

urlpatterns = [
    # path('login/', views.user_login, name='user_login'),  #使用自己写的登录视图
    path('login/', auth_views.LoginView.as_view(template_name='account/login2.html'), name='user_login'), #使用Django内置的登录视图
    path('logout', auth_views.LogoutView.as_view(), name='user_logou')


]
