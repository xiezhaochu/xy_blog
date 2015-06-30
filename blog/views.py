from django.shortcuts import render_to_response, RequestContext
from django.views.generic import View, DetailView
from django.http import HttpResponse
from blog.models import Article
from blog.forms import ArticleCreationForm
from author.models import XyUser
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
import json

class IndexView(View):
    def get(self,request):
        return render_to_response('blog/index.html', context_instance=RequestContext(request))

class PartView(View):
    def get(self, request, *args, **kwargs):
        op = self.kwargs.get('op')
        if op == 'navbar':
            return self.navbar(request)

    def navbar(self,request):
        return render_to_response('blog/include/navbar.html', context_instance=RequestContext(request))

class ArticleView(View):
    def post(self,request, *args, **kwargs):
        op = self.kwargs.get('op')
        if op == 'add':
            return self.add(request)
    
    @method_decorator(permission_required('blog.add_article'))
    def add(self,request):
        new = ArticleCreationForm(request.POST, user=request.user)
        errors = []
        if new.is_valid():
            new.save()
            return HttpResponse("发布成功")
        else:
            for k,v in new.errors.items():
                errors.append(v)
            mydict = {"errors":errors}
            return HttpResponse(json.dumps(mydict),content_type="application/json")


class EditView(View):
    def get(self, request):
        return render_to_response('blog/edit.html', context_instance=RequestContext(request))
