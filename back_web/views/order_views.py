from django.core.paginator import Paginator
from django.shortcuts import render

from back_web.models import OrderModel, DistribModel


def show_order(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        order_status = request.GET.get('order_status', 'all')
        if order_status == 'all':
            orders = OrderModel.objects.all()
        else:
            orders = OrderModel.objects.filter(o_status=order_status)
        paginator = Paginator(orders, 5)
        order_list = paginator.page(page)
        data = {
            'order_list': order_list,
            'page': page,
            'order_status': order_status,
            'num': len(order_list),
            'status_list': ['all', '0', '1', '2', '3', '4']
        }
        return render(request, 'back_web/show_order.html', data)


def edit_order(request):
    if request.method == 'GET':
        order_id = request.GET.get('order_id')
        orders = OrderModel.objects.filter(pk=order_id).first()
        distribs = DistribModel.objects.all()
        if orders:
            data = {
                'orders': orders,
                'distribs': distribs
            }
            return render(request, 'back_web/edit_order.html', data)

    if request.method == 'POST':
        order_id = request.GET.get('order_id')
        distrib_id = request.POST.get('distrib_id')
        order = OrderModel.objects.filter(pk=order_id).first()
        if order:
            order.o_status = 2
            order.distrib_id =distrib_id
            order.save()
            msg = {'msg': '修改成功'}
        else:
            msg = {'msg': '订单不存在'}
        return render(request, 'back_web/edit_order.html', msg)