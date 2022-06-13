from django.urls import path

from . import views

urlpatterns = [
    path('', views.AdminLogin.as_view(), name='login'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('task', views.TemplateTaskView.as_view(), name='task_view'),

    
]