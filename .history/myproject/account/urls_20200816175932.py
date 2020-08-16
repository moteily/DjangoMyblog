from django.urls import path
from . import views
from django.contrib.auth import  views as auth_views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login2.html'), name='user_login'),



]
