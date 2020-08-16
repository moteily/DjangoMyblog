from django.urls import path
from . import views
from django.contrib.auth 

urlpatterns = [
    path('login/', views.user_login, name='user_login'),



]
