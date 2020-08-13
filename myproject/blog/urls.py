from django.urls import path
from . import views

urlpatterns = [
    path('',views.blog_title), #第一个参数为空，表示访问根，因为在blog应用中，所以访问blog应用的根，即https://127.0.0.1:8080/blog/
    path('<int:article_id>/',views.blog_article),   #通过正则表达式确定views.blog_article为要访问的视图
]