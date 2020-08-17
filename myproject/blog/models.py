from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.


class BlogArticles(models.Model):
    title = models.CharField(max_length=300)   #字符串类型，必须要给出max_length,对应于html中的<input type="text"> 
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")  # CASCADE:级联删除，
    # 如果删除了“用户表”中某个用户，文章表中用户的文章记录也会删除
    body = models.TextField()
    # iddd = models.DateField(auto_now=...)
    publish = models.DateTimeField(default=timezone.now)
    class Meta:
        ordering = ("-publish",)  # 元组只有一个元素时，要加，

    def __str__(self):  #这两句对整个程序影响不大
        return self.title
