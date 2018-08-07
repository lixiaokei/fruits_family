from django.core.paginator import Paginator
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from back_web.models import OrderModel


# 用户中心订单显示
def user_order_info(request):
    if request.method == 'GET':
        user = request.user
        if user.id:
            page = int(request.GET.get('page', 1))
            orders = OrderModel.objects.filter(user=user).order_by('o_create')
            paginator = Paginator(orders, 5)
            order_list = paginator.page(page)
            data = {
                'order_list': order_list,
                'page': page,
                'num': len(orders),
            }
            return render(request, 'user/user_center_order.html', data)