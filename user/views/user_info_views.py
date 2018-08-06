
from django.shortcuts import render

from back_web.models import AddressModel, StaticModel


# 用户中心显示
def user_center_info(request):
    if request.method == 'GET':
        user = request.user
        logo = StaticModel.objects.filter(name='LOGO').first()
        address_list = AddressModel.objects.filter(user=user)
        data = {'user': user, 'logo': logo, 'address_list': address_list}
        return render(request, 'user/user_center_info.html', data)


# 显示收货地址
def show_address(request):
    if request.method == 'GET':
        user = request.user
        logo = StaticModel.objects.filter(name='LOGO').first()
        address_list = AddressModel.objects.filter(user=user)
        data = {'user': user, 'logo': logo, 'address_list': address_list}
        return render(request, 'user/user_center_site.html', data)


