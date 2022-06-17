from django.urls import path

from . import views

urlpatterns = [
    path('', views.AdminLogin.as_view(), name='login'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('task', views.TemplateTaskView.as_view(), name='task_view'),
    #User story model paths
    path('User_Story/create/', views.UserStoryCreate.as_view(), name='user-story-create'),
    path('User_Story/<int:pk>/update/', views.UserStoryUpdate.as_view(), name='user-story-update'),
    path('User_Story/<int:pk>/delete/', views.UserStoryDelete.as_view(), name='user-story-delete'),

    
]