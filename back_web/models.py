from django.db import models

from user.models import UserModel


# 商品分组
class GroupModel(models.Model):

    name = models.CharField(max_length=100, unique=True)
    img = models.ImageField(upload_to='group')
    icon_type = models.CharField(max_length=32, null=True)

    class Meta:
        db_table = 'tb_fruit_group'

    def edit(self, name, img):
        self.name = name if (name != self.name and name not in ('', None)) else self.name
        self.img = img if (img != self.img and img not in ('', None)) else self.img


# 商品
class GoodsModel(models.Model):
    name = models.CharField(max_length=100)     # 名称
    img = models.ImageField(upload_to='goods')  # 图片
    group = models.ForeignKey(GroupModel)       # 关联分组外键
    price = models.CharField( max_length=32, default=0.00)  # 单价
    intro = models.CharField(max_length=255, null=True)     # 简述
    format = models.CharField(max_length=32, null=True)     # 规格
    description = models.TextField(null=True)               # 详情

    class Meta:
        db_table = 'tb_fruits_good'

    def edit(self, name, img, group, price, description, intro, format):
        self.name = name if (name != self.name and name not in ('', None)) else self.name
        self.img = img if (img != self.img and img not in ('', None)) else self.img
        self.group = group if (group != self.group_id and group not in ('', None)) \
            else self.group_id
        self.price = price if (price != self.price and price not in ('', None)) else self.price
        self.description = description if \
            (description != self.description and description not in ('', None)) \
            else self.description
        self.intro = intro if (intro != self.intro and intro not in ('', None)) else self.intro
        self.format = format if (format != self.format and format not in ('', None)) \
            else self.format

    def info_dict(self):
        data = {'name': self.name, 'img': self.img}


# 静态图
class StaticModel(models.Model):
    img = models.ImageField(upload_to='static_file')  # 图片
    name = models.CharField(max_length=100)  # 名称

    class Meta:
        db_table = 'tb_static'

    def edit(self, name, img):
        self.name = name if (name != self.name and name not in ('', None)) else self.name
        self.img = img if (img != self.img and img not in ('', None)) else self.img


# 轮播图
class BannerModel(models.Model):
    img = models.ImageField(upload_to='banner')  # 图片
    name = models.CharField(max_length=100)  # 名称

    class Meta:
        db_table = 'tb_banner'

    def edit(self, name, img):
        self.name = name if (name != self.name and name not in ('', None)) else self.name
        self.img = img if (img != self.img and img not in ('', None)) else self.img


# 购物车
class CartModel(models.Model):

    good = models.ForeignKey(GoodsModel)    # 关联商品模型外键
    count = models.IntegerField(default=1)    # 商品个数
    user = models.ForeignKey(UserModel)    # 关联用户模型外键
    is_select = models.BooleanField(default=True)   # 选中状态

    class Meta:
        db_table = 'tb_cart'


# 运费模型
class FreightModel(models.Model):

    area = models.CharField(max_length=40, unique=True)  # 区域
    cost = models.CharField(max_length=10)  # 运费

    class Meta:
        db_table = 'tb_freight'


# 收货地址
class AddressModel(models.Model):

    user = models.ForeignKey(UserModel)     # 关联用户
    area = models.ForeignKey(FreightModel)   # 区域省份
    address = models.CharField(max_length=40, default='')    # 地址
    name = models.CharField(max_length=32, default='')   # 收货人姓名
    tel_phone = models.CharField(max_length=13, default='')  # 收货人电话

    class Meta:
        db_table = 'tb_user_address'

    # 编辑方法
    def edit(self, area_id, address, name, tel_phone):
        self.area_id = area_id if (area_id != self.area_id and area_id not in ('', None)) else self.area_id
        self.address = address if (address != self.address and address not in ('', None)) else self.address
        self.name = name if (name != self.name and name not in ('', None)) else self.name
        self.tel_phone = tel_phone if (tel_phone != self.tel_phone and tel_phone not in ('', None)) \
            else self.tel_phone
        self.save()


# 订单
class OrderModel(models.Model):
    user = models.ForeignKey(UserModel)  # 关联用户
    o_num = models.CharField(max_length=64)  # 订单号
    # 0 代表已下单，但是未付款， 1 已付款未发货  2 已付款，已发货.....
    o_status = models.IntegerField(default=0)  # 状态
    o_create = models.DateTimeField(auto_now_add=True)  # 创建时间
    address = models.CharField(max_length=255, default='')   # 收货地址
    cost = models.FloatField(default=10.0)                  # 运费
    name = models.CharField(max_length=20, default='')                  # 收货人姓名
    tel_phone = models.CharField(max_length=13, default='')  # 收货人电话
    total_price = models.CharField(max_length=10)   # 订单金额

    class Meta:
        db_table = 'tb_order'


# 订单商品中间表
class OrderGoodsModel(models.Model):
    goods = models.ForeignKey(GoodsModel)  # 关联的商品
    order = models.ForeignKey(OrderModel)  # 关联的订单
    goods_num = models.IntegerField(default=1)  # 商品的个数

    class Meta:
        db_table = 'tb_order_goods'


