
from django.http import JsonResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from back_web.models import CartModel, OrderModel, OrderGoodsModel, AddressModel, StaticModel
from utils.functions import order_num


# 显示订单生成页面
def make_order(request):
    if request.method == 'GET':
        user = request.user
        if user.id:
            carts = CartModel.objects.filter(user=user, is_select=True)
            logo = StaticModel.objects.filter(name='LOGO').first()
            address = AddressModel.objects.filter(user=user).first()
            cost = float(address.area.cost) if address else 0
            if carts:
                total = 0
                for info in carts:
                    total += float(info.good.price) * info.count
                data = {'cost': cost, 'total_price': total,
                        'address': address, 'logo': logo, 'carts': carts}
                return render(request, 'fruits_shop/place_order.html', data)

    if request.method == 'POST':
        user = request.user
        if user.id:
            carts = CartModel.objects.filter(user=user, is_select=True)
            if carts:
                address_id = request.POST.get('address_id')
                address_obj = AddressModel.objects.filter(pk=address_id).first()
                cost = float(address_obj.area.cost)
                address = address_obj.area.area + address_obj.address
                o_num = order_num()
                order = OrderModel.objects.create(user=user, o_num=o_num, address=address,
                                                  cost=cost, name=address_obj.name,
                                                  tel_phone=address_obj.tel_phone)
                total = 0
                for info in carts:
                    total += float(info.good.price) * info.count
                    OrderGoodsModel.objects.create(order=order, goods=info.good,
                                                   goods_num=info.count)
                carts.delete()
                order.total_price = '%.2f' % (total + cost)
                order.save()
                return HttpResponseRedirect(reverse('fruits_shop:order_pay') + '?order_id=' + str(order.id))


# 确认支付
def order_pay(request):
    if request.method == 'GET':
        order_id = request.GET.get('order_id')
        return render(request, 'fruits_shop/order_pay.html', {'order_id': order_id})

    if request.method == 'POST':
        user = request.user
        if user.id:
            order_id = request.POST.get('order_id')
            order = OrderModel.objects.filter(pk=order_id).first()
            order.o_status = 1
            order.save()
            return JsonResponse({'code': 200})
