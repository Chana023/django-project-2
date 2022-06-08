from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView 
# Create your views here.
def index(request):
    return HttpResponse("Testing")

def login_page(request):
    return render(request, 'scrumapp/login.html')

class TemplateTaskView(TemplateView):
    template_name = 'scrumapp/task.html'

    def get_context_data(self, **kwargs):
        #kwargs.setdefault('view', self)
        #if self.extra_context is not None:
        #    kwargs.update(self.extra_context)
        #return kwargs
        kwargs = super().get_context_data(**kwargs)
        kwargs['Tasks'] = ['1','2','3']
        return kwargs