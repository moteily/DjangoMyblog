from django.urls import path
from . import views
from djan

urlpatterns = [
    path('login/', views.user_login, name='user_login'),



]
