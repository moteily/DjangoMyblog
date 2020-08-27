from django.shortcuts import render
# 本文件创建视图函数：基于函数的视图
# 或者创建基于类的视图

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import BlogArticles


def blog_title(request):  # request参数负责响应所接收到的请求且不能缺少
    blogs = BlogArticles.objects.all()  # 得到所有BlogArticles类的实例
    # render()的第一个参数必须是request，然后是模板位置和所传送的数据，
    return render(request, "blog/titles.html", {"blogs": blogs})
    # 数据是使用类字典的形式传递给模板（json）


def blog_article(request, article_id):
    # article = BlogArticles.objects.get(id=article_id)
    article = get_object_or_404(BlogArticles, id=article_id)    #从model层得到数据
    pub = article.publish
    return render(request, "blog/content.html", {"article": article, "publish": pub})   #交给template层的html进行显示

