from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.generic import TemplateView 
from django.contrib.auth.views import LoginView

from scrumapp.forms import CustomUserCreationForm
# Create your views here.

def home(request):
    return render(request, 'scrumapp/home.html')

class AdminLogin(LoginView):
    template_name = 'scrumapp/login.html'

def register(request):
    if request.method == 'GET':
        return render(request, 'scrumapp/login.html', {'form': CustomUserCreationForm})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        print('test')
        if form.is_valid():
            user = form.save()
            return HttpResponse('User created')

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