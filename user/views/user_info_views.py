
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from back_web.models import AddressModel, StaticModel, FreightModel


# 用户中心显示
def user_center_info(request):
    if request.method == 'GET':
        user = request.user
        logo = StaticModel.objects.filter(name='LOGO').first()
        address_list = AddressModel.objects.filter(user=user)
        data = {'user': user, 'logo': logo, 'address_list': address_list}
        return render(request, 'user/user_center_info.html', data)


# 删除收货地址
def del_address(request):
    if request.method == 'GET':
        addr_id = request.GET.get('addr_id')
        address = AddressModel.objects.filter(id=addr_id).first()
        if address:
            address.delete()
            return HttpResponseRedirect(reverse('user:show_address'))


# 修改收货地址
def edit_address(request):
    if request.method == 'GET':
        addr_id = request.GET.get('addr_id')
        address = AddressModel.objects.filter(id=addr_id).first()
        areas = areas = FreightModel.objects.all()
        if address:
            data = {'address': address, 'areas': areas}
            return render(request, 'user/user_center_add_addr.html', data)
    if request.method == 'POST':
        area, address = request.POST.get('area'), request.POST.get('address')
        tel_phone, name = request.POST.get('tel_phone'), request.POST.get('name')
        addr_id = request.GET.get('addr_id')
        address_obj = AddressModel.objects.filter(id=addr_id).first()
        if address_obj:
            address_obj.edit(area, address, name, tel_phone)
            return HttpResponseRedirect(reverse('user:show_address'))


# 添加收货地址
def add_address(request):
    if request.method == 'GET':
        areas = FreightModel.objects.all()
        data = {'areas': areas}
        return render(request, 'user/user_center_add_addr.html', data)

    if request.method == 'POST':
        area, address = request.POST.get('area'), request.POST.get('address')
        tel_phone, name = request.POST.get('tel_phone'), request.POST.get('name')
        user = request.user
        if not all([area, address, tel_phone, name, user]):
            data = {'msg': '请填写完整信息'}
        elif not user.id:
            data = {'msg': '请登录'}
        else:
            AddressModel.objects.create(area_id=area, address=address,
                                        name=name, tel_phone=tel_phone,
                                        user=user)
            data = {'msg': '添加成功'}
        return render(request, 'user/user_center_add_addr.html', data)


# 显示收货地址
def show_address(request):
    if request.method == 'GET':
        user = request.user
        if user.id:
            logo = StaticModel.objects.filter(name='LOGO').first()
            address_list = AddressModel.objects.filter(user=user)
            data = {'user': user, 'logo': logo, 'address_list': address_list}
            return render(request, 'user/user_center_site.html', data)


