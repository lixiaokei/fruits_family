from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^user_center_info/', views.user_center_info, name='user_center_info'),
    url(r'^show_address/', views.show_address, name='show_address'),
    url(r'^add_address/', views.add_address, name='add_address'),
    url(r'^edit_address/', views.edit_address, name='edit_address'),
    url(r'^del_address/', views.del_address, name='del_address'),
    url(r'^user_order_info/',views.user_order_info, name='user_order_info'),


]
