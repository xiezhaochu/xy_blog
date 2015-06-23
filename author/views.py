#coding:utf-8
from django.shortcuts import render, render_to_response
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.views.generic import View
from author.forms import XyUserCreationForm
from django.contrib import auth
from django.template import RequestContext
import json
class UserControl(View):
    def post(self, request, *args, **kwargs):
        op = self.kwargs.get('op')
        if op == 'register':
            return self.register(request)
        elif op == 'login':
            return self.login(request)
        elif op == 'logout':
            return self.logout(request)

    def get(self, request, *args, **kwargs):
        op = self.kwargs.get('op')
        if op == 'logout':
            return self.logout(request)
        
    def register(self, request):
        newuser = XyUserCreationForm(request.POST)
        errors = []
        if newuser.is_valid():
            newuser.save()
            return HttpResponse(u"注册成功")
        else:
            for k,v in newuser.errors.items():
                errors.append(v.as_text())

        mydict = {"errors":errors}
        return HttpResponse(json.dumps(mydict),content_type="application/json")

    def login(self, request):
        username = request.POST.get("username","")
        password = request.POST.get("password","")
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            user = auth.login(request,user)
            return HttpResponseRedirect("/")
        else:
            return HttpResponse(u"密码错误")

    def logout(self, request):
        auth.logout(request)
        return HttpResponseRedirect("/")

class UserForm(View):
    def get(self, request, *args, **kwargs):
        op = self.kwargs.get('op')
        if op == 'register':
            return self.register(request)
        elif op == 'login':
            return self.login(request)

    def register(self, request):
        f = XyUserCreationForm()
        return render_to_response('author/register.html',{'f':f},context_instance=RequestContext(request))

    def login(self, request):
        return render_to_response('author/login.html', context_instance=RequestContext(request))
