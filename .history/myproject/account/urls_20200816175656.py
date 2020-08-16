from django.urls import path
from . import views
from djang

urlpatterns = [
    path('login/', views.user_login, name='user_login'),



]
