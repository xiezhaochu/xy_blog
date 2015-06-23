from django.conf.urls import url
from author.views import UserControl,UserForm
from django.views.generic import TemplateView
urlpatterns = [
        url(r'^u/(?P<op>\w+)$',UserControl.as_view(), name = "UserControl"),
        url(r'^f/(?P<op>\w+)$',UserForm.as_view(), name = "UserForm")
#        url(r'^$',TemplateView.as_view(template_name = 'author/register.html'))
]
