from django.db import models
from author.models import XyUser

class Article(models.Model):
    STATUS = {
        0:u'发布',
        1:u'草稿',
        2:u'删除',
    }
    author = models.ForeignKey(XyUser)
    title = models.CharField(max_length=50)
    tags = models.CharField(max_length=100,null=True,blank=True)
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0, choices=STATUS.items())
    class Meta:
        ordering = ['-create_time']

