from django.shortcuts import render_to_response, RequestContext, get_object_or_404, render
from django.views import generic
from django.http import HttpResponse
from blog.models import Article
from blog.forms import ArticleCreationForm
from author.models import XyUser
from django.contrib.auth.decorators import permission_required
from django.utils.decorators import method_decorator
import json

class Index(generic.ListView):
    context_object_name = "article_list"
    template_name = "blog/index.html"
    model = Article
    paginate_by = 2

class Part(generic.View):
    def get(self, request, *args, **kwargs):
        op = self.kwargs.get('op')
        if op == 'navbar':
            return self.navbar(request)

    def navbar(self,request):
        return render_to_response('blog/include/navbar.html', context_instance=RequestContext(request))

class ArticleControl(generic.View):
    def post(self,request, *args, **kwargs):
        op = self.kwargs.get('op')
        if op == 'create':
            return self.create(request)
        if op == 'update':
            return self.update(request, **kwargs)
    
    @method_decorator(permission_required('blog.add_article'))
    def create(self, request):
        form = ArticleCreationForm(request.POST, user=request.user)
        errors = []
        if form.is_valid():
            form.save()
            return HttpResponse("发布成功")
        else:
            for k,v in form.errors.items():
                errors.append(v)
            mydict = {"errors":errors}
            return HttpResponse(json.dumps(mydict),content_type="application/json")
    
    def update(self,request, **kwargs):
        id = kwargs.get('id')
        article = get_object_or_404(Article, pk= id)
        form = ArticleCreationForm(request.POST, instance=article, user=article.author)
        if form.is_valid():
            form.save()
            return HttpResponse("修改成功")
        else:
            for k,v in form.errors.items():
                errors.append(v)
            mydict = {"errors":errors}
            return HttpResponse(json.dumps(mydict),content_type="application/json")

class Detail(generic.DetailView):
    model = Article

class Edit(generic.View):
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        if id != "":
            article = get_object_or_404(Article, pk=id)
            return render(request, 'blog/edit_update.html', {"article":article})
        else:
            return render_to_response('blog/edit_create.html', context_instance=RequestContext(request))
