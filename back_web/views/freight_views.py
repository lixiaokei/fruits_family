
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.urls import reverse

from back_web.models import FreightModel


# 显示运费设置信息
def show_freight(request):
    if request.method == 'GET':
        freights = FreightModel.objects.all()
        page = int(request.GET.get('page', 1))
        paginator = Paginator(freights, 5)
        freight_list = paginator.page(page)
        data = {
            'freight_list': freight_list,
            'page': page,
            'num': len(freight_list),
        }
        return render(request, 'back_web/show_freight.html', data)
    raise Http404


# 添加运费设置
def add_freight(request):
    if request.method == 'GET':
        return render(request, 'back_web/add_freight.html')

    if request.method == 'POST':
        address = request.POST.get('address')
        freight = request.POST.get('freight')
        if not all([address, freight]):
            msg = {'msg': '请填写完整信息'}
        if FreightModel.objects.filter(area=address).exists():
            msg = {'msg': '区域地质重复'}
        else:
            FreightModel.objects.create(area=address, cost=freight)
            msg = {'msg': '添加成功'}
        return render(request, 'back_web/add_freight.html', msg)