from django.urls import path
from . import views
from django.contrib.auth import  views

urlpatterns = [
    path('login/', views.user_login, name='user_login'),
    path('login/', auth, name=str)



]
