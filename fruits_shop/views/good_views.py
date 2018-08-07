
from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

from back_web.models import BannerModel, StaticModel, GroupModel,\
    GoodsModel
from utils.functions import random_list


class FruitShopView(ListView):
    """商店商品显示视图类"""
    template_name = 'fruits_shop/index.html'
    context_object_name = 'groups'
    model = GroupModel

    def get_context_data(self, **kwargs):
        kwargs['banners'] = BannerModel.objects.all()
        kwargs['statics'] = StaticModel.objects.all()
        kwargs['logo'] = StaticModel.objects.filter(name='LOGO').first()
        return super(FruitShopView, self).get_context_data(**kwargs)


# 商品详情页面
def fruit_detail(request):
    if request.method == 'GET':
        good_id = request.GET.get('good_id')
        good = GoodsModel.objects.filter(pk=good_id).first()
        logo = StaticModel.objects.filter(name='LOGO').first()
        groups = GroupModel.objects.all()
        goods_list = GoodsModel.objects.filter(~Q(pk=good_id))
        others = random_list(goods_list)
        data = {
            'good': good,
            'logo': logo,
            'groups': groups,
            'others': others,
        }
        return render(request, 'fruits_shop/detail.html', data)

