from django.shortcuts import render_to_response, RequestContext
from django.views.generic import View, DetailView
from django.http import HttpResponse

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
