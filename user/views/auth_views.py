import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.hashers import make_password, check_password
from django.urls import reverse

from user.models import UserModel, UserTicketModel
from utils.functions import random_session


# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')

    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        msg = {}
        if UserModel.objects.filter(username=user_name).exists():
            msg['code'], msg['msg'] = 302, '用户名已存在'
        password1 = request.POST.get('pwd')
        password2 = request.POST.get('pwd2')
        if password1 != password2:
            msg['code'], msg['msg'] = 302, '两次密码不一致。'
        password = make_password(password1)
        email = request.POST.get('email')
        UserModel.objects.create(username=user_name,
                                 password=password,
                                 email=email)
        msg['code'], msg['msg'] = 200, '用户注册成功'
        return render(request, 'user/register.html', msg)
    return render(request, None)


# 登陆
def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        msg = {}
        if not all([username, password]):
            return render(request, 'user/login.html',
                          {'code': 302, 'msg': '输入错误'})
        if UserModel.objects.filter(username=username).exists():
            user = UserModel.objects.filter(username=username).first()
            if check_password(password, user.password) and not user.is_delete:
                session_id = random_session(30)
                res = HttpResponseRedirect(reverse('fruits_shop:index'))
                res.set_cookie('session_id', session_id, max_age=60000)
                out_time = datetime.datetime.now() + datetime.timedelta(hours=1)
                UserTicketModel.objects.create(user=user,
                                               session_id=session_id,
                                               out_time=out_time)
                return res
            else:
                msg['msg'], msg['code'] = 302, '用户名密码错误，请重新登陆'
        else:
            msg['msg'], msg['code'] = 302, '用户名密码错误，请重新登陆'
        return render(request, 'user/login.html', msg)
