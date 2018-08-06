
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


from back_web.models import BannerModel


# 删除轮播文件
def del_banner(request):
    if request.method == 'GET':
        banner_id = request.GET.get('banner_id')
        banner = BannerModel.objects.filter(pk=banner_id).first()
        if banner:
            banner.delete()
        return HttpResponseRedirect(reverse('back_web:show_banner'))


# 编辑轮播文件
def edit_banner(request):
    if request.method == 'GET':
        banner_id = request.GET.get('banner_id')
        banner = BannerModel.objects.filter(pk=banner_id).first()
        if banner:
            return render(request, 'back_web/add_banner.html',
                          {'banner': banner, 'msg': '不改可不填'})
    if request.method == 'POST':
        banner_id = request.GET.get('banner_id')
        banner = BannerModel.objects.filter(pk=banner_id).first()
        if banner:
            name, img = request.POST.get('name'), request.FILES.get('img', '')
            banner.edit(name=name, img=img)
            banner.save()
        return HttpResponseRedirect(reverse('back_web:show_static'))


# 显示轮播图
def show_banner(request):
    if request.method == 'GET':
        banners = BannerModel.objects.all()
        page = int(request.GET.get('page', 1))
        paginator = Paginator(banners, 5)
        banner_list = paginator.page(page)
        data = {
            'banner_list': banner_list,
            'page': page,
            'num': len(banner_list),
        }
        return render(request, 'back_web/show_banner.html', data)


# 添加轮播图
def add_banner(request):
    if request.method == 'GET':
        return render(request, 'back_web/add_banner.html')

    if request.method == 'POST':
        name, img = request.POST.get('name'), request.FILES.get('img')
        banner = BannerModel.objects.filter(name=name).first()
        if banner:
            return render(request, 'back_web/add_banner.html', {'msg': '名称已存在'})
        BannerModel.objects.create(name=name, img=img)
        return HttpResponseRedirect(reverse('back_web:show_banner'))