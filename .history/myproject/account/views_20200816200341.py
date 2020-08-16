from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login #authenticate:证明...是真实的
from .forms import LoginForm

# Create your views here.
def user_login(request):
    if request.method == "POST":
        if request.us
        login_form = LoginForm(request.POST)
        if login_form.is_valid():   #检查表格项中参数的值不能为空
            cd = login_form.cleaned_data
            user = authenticate(password=cd['password'], username=cd['username'])   #检验此用户是否为本网站项目的用户(admin界面创建)以
            #及密码是否正确,正确则返回User的一个实例对象
            if user:
                login(request, user)    #对上面得到的User实例对象user作为参数，实现用户登陆。用户登陆之后，Django会自动调用默认的session应用，
                #将用户的ID保存在session中，完成用户登陆操作,通常情况下login()和authenticate()配合使用
                return HttpResponse("Welcome You. If you hava a dream.Don't lose it. Just do it!\n You have been authenticated successfully")
            else:
                return HttpResponse("Sorry.Your username or password is not right.")
        else:
            return HttpResponse("Invalid login.")
    if request.method == "GET":
        login_form = LoginForm()
        return render(request,"account/login.html",{"form":login_form})