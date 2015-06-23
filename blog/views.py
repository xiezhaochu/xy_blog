from django.shortcuts import render_to_response, RequestContext
from django.views.generic import View
from django.http import HttpResponse

class IndexView(View):
    def get(self,request):
        return render_to_response('blog/index.html', context_instance=RequestContext(request))
