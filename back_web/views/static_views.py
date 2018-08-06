
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from back_web.models import StaticModel


# 删除静态文件
def del_static(request):
    if request.method == 'GET':
        static_id = request.GET.get('static_id')
        static = StaticModel.objects.filter(pk=static_id).first()
        if static:
            static.delete()
        return HttpResponseRedirect(reverse('back_web:show_static'))


# 编辑静态文件
def edit_static(request):
    if request.method == 'GET':
        static_id = request.GET.get('static_id')
        static = StaticModel.objects.filter(pk=static_id).first()
        if static:
            return render(request, 'back_web/add_static.html',
                          {'static': static, 'msg': '不改可不填'})
    if request.method == 'POST':
        static_id = request.GET.get('static_id')
        static = StaticModel.objects.filter(pk=static_id).first()
        if static:
            name, img = request.POST.get('name'), request.FILES.get('img', '')
            static.edit(name=name, img=img)
            static.save()
        return HttpResponseRedirect(reverse('back_web:show_static'))


# 显示静态文件
def show_static(request):
    if request.method == 'GET':
        statics = StaticModel.objects.all()
        page = int(request.GET.get('page', 1))
        paginator = Paginator(statics, 5)
        static_list = paginator.page(page)
        data = {
            'static_list': static_list,
            'page': page,
            'num': len(static_list),
        }
        return render(request, 'back_web/show_static.html', data)


# 添加静态文件
def add_static(request):
    if request.method == 'GET':
        return render(request, 'back_web/add_static.html')

    if request.method == 'POST':
        name = request.POST.get('name')
        img = request.FILES.get('img', '')
        if StaticModel.objects.filter(name=name).exists():
            return render(request, 'back_web/add_static.html', {'msg': '名称已存在'})
        StaticModel.objects.create(name=name, img=img)
        return HttpResponseRedirect(reverse('back_web:show_static'))