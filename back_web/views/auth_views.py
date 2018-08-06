from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# 登陆
def login(request):

    if request.method == 'GET':
        return render(request, 'back_web/login.html')
    if request.method == 'POST':
        name = request.POST.get('user')
        pwd = request.POST.get('pwd')
        user = auth.authenticate(username=name, password=pwd)
        if user:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('back_web:index'))
        return render(request, 'back_web/login.html',
                      {'msg': '用户名密码错误'})


# 注销
def logout(request):
    if request.method == 'GET':
        auth.logout(request)
        return HttpResponseRedirect(reverse('back_web:login'))