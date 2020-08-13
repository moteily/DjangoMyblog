from django.contrib import admin
from .models import BlogArticles 


class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title","author","publish")
    list_filter = ("publish","author")
    search_fields = ("title","body")
    raw_id_fields = ("author",) #注意逗号，显示外键信息
    date_hierarchy = "publish"  #hierarchy ：层次，等级制度
    ordering = ['-publish','author']

admin.site.register(BlogArticles,BlogArticlesAdmin)


# Register your models here.
