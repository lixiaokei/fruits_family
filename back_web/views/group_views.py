
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from back_web.models import GroupModel


# 删除分组
def del_group(request):
    if request.method == 'GET':
        group_id = request.GET.get('group_id')
        group = GroupModel.objects.filter(pk=group_id)
        if group:
            group.delete()
        return HttpResponseRedirect(reverse('back_web:show_group'))


# 显示分组信息
def show_group(request):
    if request.method == 'GET':
        page = int(request.GET.get('page', 1))
        groups = GroupModel.objects.all()
        paginator = Paginator(groups, 5)
        group_list = paginator.page(page)
        data = {
            'group_list': group_list,
            'page': page,
            'num': len(groups)
        }
        return render(request, 'back_web/show_group.html', data)


# 编辑分组
def edit_group(request):
    if request.method == 'GET':
        group_id = request.GET.get('group_id')
        group = GroupModel.objects.filter(pk=group_id).first()
        if group:
            return render(request,
                          'back_web/add_group.html',
                          {'msg': '不改可不填', 'group': group})
    if request.method == 'POST':
        group_id = request.GET.get('group_id')
        group = GroupModel.objects.filter(pk=group_id).first()
        if group:
            name, img = request.POST.get('group_name'), request.FILES.get('group_img', '')
            group.edit(name=name, img=img)
            group.save()
            return HttpResponseRedirect(reverse('back_web:show_group'))


# 添加分组
def add_group(request):
    if request.method == 'GET':
        return render(request, 'back_web/add_group.html')
    if request.method == 'POST':
        group_name = request.POST.get('group_name')
        group_img = request.FILES.get('group_img', '')
        if GroupModel.objects.filter(name=group_name).exists():
            msg = {'code': 302, 'msg': '分组已存在'}
            return render(request, 'back_web/add_group.html', msg)
        GroupModel.objects.create(name=group_name, img=group_img)
        msg = {'code': 200, 'msg': '分组添加成功'}
        return render(request, 'back_web/add_group.html', msg)
    else:
        return render(request, None)