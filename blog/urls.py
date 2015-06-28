from django.conf.urls import url
from blog.views import *
urlpatterns = [
    url(r'^$',IndexView.as_view(),name="index"),
    url(r'^p/(?P<op>\w+)$',PartView.as_view(),name="part"),
]
