from django.urls import path
from . import views
from django 

urlpatterns = [
    path('login/', views.user_login, name='user_login'),



]
