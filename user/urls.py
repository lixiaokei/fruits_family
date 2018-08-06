from django.conf.urls import url

from user import views

urlpatterns = [
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^user_center_info/', views.user_center_info, name='user_center_info'),
    url(r'^show_address/', views.show_address, name='show_address'),]
