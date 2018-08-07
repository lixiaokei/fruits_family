
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from back_web.models import GoodsModel, GroupModel


# 显示商品&首页
def index(request):
    if request.method == 'GET':
        goods = GoodsModel.objects.all()
        page = int(request.GET.get('page', 1))
        paginator = Paginator(goods, 5)
        good_list = paginator.page(page)
        data = {
            'good_list': good_list,
            'page': page,
            'num': len(goods),
        }
        return render(request, 'back_web/index.html', data)


# 编辑商品
def edit_good(request):
    if request.method == 'GET':
        good_id = request.GET.get('good_id')
        good = GoodsModel.objects.filter(pk=good_id).first()
        if good:
            group_list = GroupModel.objects.all()
            return render(request, 'back_web/add_goods.html',
                          {'group_list': group_list, 'good': good,
                           'msg': '不改可不填'})
    if request.method == 'POST':
        good_id = request.GET.get('good_id')
        good = GoodsModel.objects.filter(pk=good_id).first()
        if good:
            name, description = request.POST.get('name'), request.POST.get('description')
            img, price = request.FILES.get('img', ''), request.POST.get('price')
            intro, format = request.POST.get('intro'), request.POST.get('format')
            group_id = request.POST.get('group')
            group = GroupModel.objects.filter(pk=group_id).first()
            good.edit(name=name, img=img, group=group, price=price,
                      description=description, intro=intro, format=format)
            good.save()
            return HttpResponseRedirect(reverse('back_web:index'))


# 删除商品
def del_good(request):
    if request.method == 'GET':
        good_id = request.GET.get('good_id')
        good = GoodsModel.objects.filter(pk=good_id)
        if good:
            good.delete()
        return HttpResponseRedirect(reverse('back_web:index'))


# 添加商品
def add_goods(request):
    if request.method == 'GET':
        group_list = GroupModel.objects.all()
        return render(request, 'back_web/add_goods.html', {'group_list': group_list})
    if request.method == 'POST':
        good_name = request.POST.get('name')
        group_id = request.POST.get('group')
        price = request.POST.get('price')
        img = request.FILES.get('img', '')
        intro = request.POST.get('intro')
        format = request.POST.get('format')
        description = request.POST.get('description')
        data = {'group_list': GroupModel.objects.all()}
        if GoodsModel.objects.filter(name=good_name).exists():
            data['msg'] = '商品名称重复'
        else:
            GoodsModel.objects.create(
                name=good_name, group_id=group_id, price=price,
                img=img, description=description, intro=intro, format=format)
            data['msg'] = '添加商品成功'
        return render(request, 'back_web/add_goods.html', data)

