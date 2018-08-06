import datetime
import re

from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from user.models import UserTicketModel
from django.core.urlresolvers import reverse


# 定义后台页面中间件验证
class BackWebMiddleware(MiddlewareMixin):

    def process_request(self, request):
        pass_path = ['/back_web/', '/back_web/login/', 'back_web/logout/']

        if re.match('^/back_web/', request.path):
            if request.path not in pass_path:
                user = request.user
                if user and user.is_authenticated():
                    return None
                else:
                    return HttpResponseRedirect(reverse('back_web:login'))
            else:
                return None


# 定义前台页面中间件类
class UserMiddleware(MiddlewareMixin):

    def process_request(self, request):
        path1 = ['/fruits_shop/index/', '/fruits_shop/detail/',
                 '/fruits_shop/add_cart/', '/fruits_shop/get_cart_count/',
                 '/fruits_shop/cart/', '/fruits_shop/subtotal/',
                 '/fruits_shop/total_price/', '/fruits_shop/change_num/',
                 '/fruits_shop/cart_delete/', '/fruits_shop/change_status/',
                 '/user/user_center_info/', '/user/show_address/',
                 '/user/add_address/', '/user/edit_address']
        path2 = ['/user/user_center_info/', '/user/show_address/',
                 '/user/add_address/', '/user/edit_address/']
        now_time = datetime.datetime.now()
        if request.path in path1:
            session_value = request.COOKIES.get('session_id')
            # 判断session是否有值
            if session_value:
                session = UserTicketModel.objects.filter(session_id=session_value).first()
                # 判断session在session表中有并且反查的user没有被删除
                if session and not session.user.is_delete:
                    if session.out_time >= now_time:
                        request.user = session.user
                        return None
                    else:
                        session.delete()
                        return None
                else:
                    if request.path in '/user/user_center_info/':
                        return HttpResponseRedirect(reverse('user:login'))
                    return None
            else:
                if request.path in '/user/user_center_info/':
                    return HttpResponseRedirect(reverse('user:login'))
                return None
        return None
