import datetime
import re

from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseRedirect
from user.models import UserTicketModel
from django.core.urlresolvers import reverse

from utils.conf import USER_MUST_LOGIN_PATH, USER_PATH_PASS

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
        now_time = datetime.datetime.now()
        if request.path in USER_PATH_PASS:
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
                    if request.path in USER_MUST_LOGIN_PATH:
                        return HttpResponseRedirect(reverse('user:login'))
                    return None
            else:
                if request.path in USER_MUST_LOGIN_PATH:
                    return HttpResponseRedirect(reverse('user:login'))
                return None
        return None
