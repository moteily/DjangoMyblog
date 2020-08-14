from django.urls import path
from . import views

urlpatterns = [path('login/', view.user_login, name='user_login')]