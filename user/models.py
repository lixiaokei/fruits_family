
from django.db import models


class UserModel(models.Model):

    username = models.CharField(max_length=20, unique=True)    # 用户名
    password = models.CharField(max_length=255, db_column='passwd')    # 密码
    email = models.CharField(max_length=64)    # 邮箱
    is_delete = models.BooleanField(default=False)    # 删除状态

    class Meta:
        db_table = 'tb_fruits_user'


class UserTicketModel(models.Model):
    user = models.ForeignKey(UserModel)  # 关联用户
    session_id = models.CharField(max_length=256)   # session_id
    out_time = models.DateTimeField()  # 过期时间

    class Meta:
        db_table = 'tb_fruits_users_ticket'

