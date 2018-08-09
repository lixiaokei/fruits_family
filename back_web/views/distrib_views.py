
from django.core.paginator import Paginator
from django.shortcuts import render

from back_web.models import DistribModel


# 删除配送方式
def del_distrib(request):
    if request.method == 'GET':
        distrib_id = request.GET.get('distrib_id')
        distrib = DistribModel.objects.filter(pk=distrib_id)
        if distrib:
            distrib.delete()


# 添加配送方式
def add_distrib(request):
    if request.method == 'GET':
        return render(request, 'back_web/add_distrib.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        img = request.FILES.get('img')
        DistribModel.objects.create(name=name, img=img)
        msg = {'msg': '添加成功'}
        return render(request, 'back_web/add_distrib.html', msg)


# 显示配送方式
def show_distrib(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        distribs = DistribModel.objects.all()
        paginator = Paginator(distribs, 5)
        distrib_list = paginator.page(page)
        data = {
            'distrib_list': distrib_list,
            'page': page,
            'num': len(distrib_list),
        }
        return render(request, 'back_web/show_distrib.html', data)