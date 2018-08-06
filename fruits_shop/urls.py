from django.conf.urls import url

from fruits_shop import views

urlpatterns = [
    url(r'^index/', views.FruitShopView.as_view(), name='index'),
    url(r'^detail/', views.fruit_detail, name='detail'),
    url(r'^change_num/', views.change_num, name='change_num'),
    url(r'^add_cart/', views.add_cart, name='add_cart'),
    url(r'^get_cart_count/', views.get_cart_count, name='get_cart_count'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^subtotal/', views.subtotal, name='subtotal'),
    url(r'^total_price/', views.total_price, name='total_price'),
    url(r'^cart_delete/', views.cart_delete, name='cart_delete'),
    url(r'^change_status/', views.change_status, name='change_status'),

]
