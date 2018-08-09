from django import template

from back_web.models import StaticModel, FreightModel, GroupModel
register = template.Library()


# 乘积过滤器
@register.filter(name='sum_tag')
def sum_tag(value, arg):
    return float(value) * int(arg)


# 浮点加法过滤器
@register.filter(name='sum')
def get_sum(value, arg):
    return float(value) + float(arg)


# 比较过滤器
@register.filter(name='equal')
def com_equal(value, arg):
        if value == arg:
            return True
        else:
            return False


# 获取指定分组的的商品信息
@register.filter(name='list')
def get_good_list(group_id):
    group = GroupModel.objects.filter(pk=group_id).first()
    if group:
        good_list = group.goodsmodel_set.all().order_by('-id')[0:4]
        return good_list

# 获取地址列表
@register.assignment_tag(name='logo')
def get_logo():
    logo = StaticModel.objects.filter(name='LOGO').first()
    return logo.img


# 区域列表
@register.assignment_tag(name='get_areas')
def get_areas():
    return FreightModel.objects.all()