from django import template

from back_web.models import StaticModel, FreightModel
register = template.Library()


# 乘积过滤器
@register.filter(name='sum_tag')
def sum_tag(value, arg):
    return float(value) * int(arg)


# 获取地址列表
@register.assignment_tag(name='logo')
def get_logo():
    logo = StaticModel.objects.filter(name='LOGO').first()
    return logo.img


# 区域列表
@register.assignment_tag(name='get_areas')
def get_areas():
    return FreightModel.objects.all()