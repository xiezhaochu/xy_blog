from django.conf.urls import url
from blog.views import *
urlpatterns = [
    url(r'^$',Index.as_view(),name="index"),
    url(r'^part/(?P<op>\w+)/$',Part.as_view(), name="part"),
    url(r'^edit/(?P<id>\d*)/?$',Edit.as_view(), name="edit"),
    url(r'^article/(?P<op>\w+)/(?P<id>[0-9]*)/?$',ArticleControl.as_view(), name="article"),
    url(r'^detail/(?P<pk>[0-9]+)/$',Detail.as_view(), name="detail"),
]
