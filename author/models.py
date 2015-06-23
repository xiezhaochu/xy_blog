#coding:utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
class XyUser(AbstractUser):
    img = models.CharField(max_length=200, default='static/tx/default.jpg',verbose_name=u'头像地址')
    class Meta(AbstractUser.Meta):
        pass
