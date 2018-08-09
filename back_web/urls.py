from django.conf.urls import url

from back_web import views

urlpatterns = [
    # 登陆
    url(r'^$', views.login, name='login'),
    url(r'^login/', views.login),
    # 注销
    url(r'^logout/', views.logout, name='logout'),

    # 首页 即商品列表
    url(r'^index/', views.index, name='index'),
    # 添加商品
    url(r'^add_goods/', views.add_goods, name='add_goods'),
    # 编辑商品
    url(r'^edit_good/', views.edit_good, name='edit_good'),
    # 删除商品
    url(r'^del_good/', views.del_good, name='del_good'),

    # 添加分组
    url(r'^add_group/', views.add_group, name='add_group'),
    # 显示分组信息
    url(r'^show_group/', views.show_group, name='show_group'),
    # 删除分组
    url(r'^del_group/',views.del_group, name='del_group'),
    # 编辑分组信息
    url(r'^edit_group/', views.edit_group, name='edit_group'),

    # 添加静态文件
    url(r'^add_static/', views.add_static, name='add_static'),
    # 显示静态文件
    url(r'^show_static/', views.show_static, name='show_static'),
    # 编辑静态文件
    url(r'^edit_static/', views.edit_static, name='edit_static'),
    # 删除静态文件
    url(r'^del_static/',views.del_static, name='del_static'),

    # 添加轮播文件
    url(r'^add_banner/', views.add_banner, name='add_banner'),
    # 显示轮播文件
    url(r'^show_banner/', views.show_banner, name='show_banner'),
    # 编辑轮播文件
    url(r'^edit_banner/', views.edit_banner, name='edit_banner'),
    # 删除轮播文件
    url(r'^del_banner/', views.del_banner, name='del_banner'),

    # 添加运费
    url(r'^add_freight/', views.add_freight, name='add_freight'),
    # 显示运费设置
    url(r'^show_freight/', views.show_freight, name='show_freight'),

    # 后台订单显示
    url(r'^show_order/', views.show_order, name='show_order'),

    # 显示配送方式
    url(r'^show_distrib/', views.show_distrib, name='show_distrib'),
    # 添加配送方式
    url(r'^add_distrib/', views.add_distrib, name='add_distrib'),
    # 删除url
    url(r'^del_distrib/', views.del_distrib, name='del_distrib'),

]
