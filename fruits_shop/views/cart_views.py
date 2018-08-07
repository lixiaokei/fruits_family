
from django.http import JsonResponse
from django.shortcuts import render

from back_web.models import StaticModel, GoodsModel, CartModel


# 改变个数api
def change_num(request):
    if request.method == 'GET':
        change_type = request.GET.get('change_type')
        value = int(request.GET.get('value'))
        good_id = request.GET.get('good_id')
        if change_type == '1':
            value += 1
        elif change_type == '0':
            if value > 1:
                value -= 1
        good = GoodsModel.objects.filter(pk=good_id).first()
        total = value * float(good.price)
        total = '%.2f' % total

        user = request.user
        if user.id:
            cart = CartModel.objects.filter(good_id=good_id, user=user).first()
            if cart:
                cart.count = value
                cart.save()
                return JsonResponse({'code': 200, 'value': value, 'total': total})

        return JsonResponse({'code': 200, 'value': value, 'total': total})


# 添加至购物车
def add_cart(request):
    if request.method == 'GET':
        user = request.user
        if user.id:
            num = int(request.GET.get('num'))
            good_id = request.GET.get('good_id')
            cart = CartModel.objects.filter(good_id=good_id, user=user).first()
            if cart:
                cart.count += num
                cart.save()
            else:
                CartModel.objects.create(good_id=good_id, user=user, count=num)
            return JsonResponse({'code': 200})
        return JsonResponse({'code': 302})


# 购物车显示接口
def get_cart_count(request):
    if request.method == 'GET':
        user = request.user
        if user.id:
            cart_list = CartModel.objects.filter(user=user)
            count = 0
            for cart in cart_list:
                count += cart.count
            return JsonResponse({'code': 200, 'count': count})
        return JsonResponse({'code': 302})


# 显示购物车页面数据
def cart(request):
    if request.method == 'GET':
        user = request.user
        logo = StaticModel.objects.filter(name='LOGO').first()
        data = {'logo': logo}
        if user.id:
            cart_list = CartModel.objects.filter(user=user)
            all_select = True
            for cart in cart_list:
                if not cart.is_select:
                    all_select =False
                    break
            data['cart_list'] = cart_list
            data['all_select'] = all_select
        else:
            data['msg'] = '请登录后查看购物车'
        return render(request, 'fruits_shop/cart.html', data)


# 购物车小计接口
def subtotal(request):
    if request.method == 'GET':
        user = request.user
        if user.id:
            cart_list = CartModel.objects.filter(user=user)
            total_list = []
            for cart in cart_list:
                tmp = {}
                tmp['cart_id'] = cart.id
                total = float(cart.good.price) * cart.count
                tmp['total'] = '%.2f' % total
                total_list.append(tmp)
            data = {'code': 200, 'total_list': total_list}
        else:
            data = {'code': 302}
        return JsonResponse(data)


# 总价计价接口
def total_price(request):
    if request.method == 'GET':
        user = request.user
        if user.id:
            cart_list = CartModel.objects.filter(user=user, is_select=True)
            total, count, all_count = 0, 0, 0
            for cart in CartModel.objects.filter(user=user):
                all_count += cart.count
            for cart in cart_list:
                total += float(cart.good.price) * cart.count
                count += cart.count
            total = '%.2f' % total
            data = {'code': 200, 'total': total, 'count': count, 'all_count': all_count}
        else:
            data = {'code': 302}
        return JsonResponse(data)


# 购物车订单删除
def cart_delete(request):
    if request.method == 'GET':
        user = request.user
        cart_id = request.GET.get('cart_id')
        if user.id:
            cart_info = CartModel.objects.filter(id=cart_id, user=user)
            if cart_info:
                cart_info.delete()
                data = {'code': 200}
            else:
                data = {'code': 302}
        else:
            data = {'code': 302}
        return JsonResponse(data)


# 勾选--全选
def change_status(request):
    if request.method == 'POST':
        user = request.user
        if user.id:
            all_change_status = True if request.POST.get('all_change_status') == 'true' \
                else False
            if all_change_status:
                all_value = True if request.POST.get('all_value') == 'true' else False
                cart_list = CartModel.objects.filter(user=user)
                for cart in cart_list:
                    cart.is_select = all_value
                    cart.save()
                data = {'code': 200}
            else:
                cart_id = request.POST.get('cart_id')
                status = True if request.POST.get('change_status') == 'true' else False
                CartModel.objects.filter(user=user, id=cart_id).update(is_select=status)
                data = {'code': 200}
        else:
            data = {'code': 302}
        return JsonResponse(data)


