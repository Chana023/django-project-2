from django.urls import path

from . import views

urlpatterns = [
    path('login', views.AdminLogin.as_view(), name='login'),
    path('logout', views.AdminLogout.as_view(), name='logout'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
    path('task', views.TemplateTaskView.as_view(), name='task_view'),
    #User story model paths
    path('User_Story/create/', views.UserStoryCreate.as_view(), name='user-story-create'),
    path('User_Story/<int:pk>/update/', views.UserStoryUpdate.as_view(), name='user-story-update'),
    path('User_Story/<int:pk>/delete/', views.UserStoryDelete.as_view(), name='user-story-delete'),
    path('User_Story/list/', views.UserStoryListView.as_view(), name = 'user-story-list'),
    path('User_Story/detail/<int:pk>', views.UserStoryDetailView.as_view(), name = 'user-story-detail'),
    #Task model paths
    path('Task/create/', views.TaskCreateView.as_view(), name='task-create'),
    path('Task/<int:pk>/update/', views.TaskUpdate.as_view(), name='task-update'),
    path('Task/<int:pk>/delete/',views.TaskDelete.as_view(), name='task-delete'),
    path('Task/list/', views.TaskListView.as_view(), name='task-list'),
    path('Task/detail/<int:pk>', views.TaskDetailView.as_view(), name='task-detail')

    
]