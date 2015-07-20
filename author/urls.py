from django.conf.urls import url
from author.views import UserControl,UserForm
from django.views.generic import TemplateView
urlpatterns = [
        url(r'^user/(?P<op>\w+)$',UserControl.as_view(), name = "UserControl"),
        url(r'^form/(?P<op>\w+)$',UserForm.as_view(), name = "UserForm")
]
