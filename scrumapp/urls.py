from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('login', views.AdminLogin.as_view(), name='login'),
    path('logout', views.AdminLogout.as_view(), name='logout'),
    path('home', views.home, name='home'),
    path('register', views.register, name='register'),
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
    path('Task/detail/<int:pk>', views.TaskDetailView.as_view(), name='task-detail'),
    #API
    path('api', views.api_root),

    path('api/task/', views.TaskList.as_view(), name='api-task-list'),
    path('api/task/<int:pk>/', views.TaskDetail.as_view(), name='api-task-detail'),
    path('api/task/<int:pk>/complete', views.TaskComplete.as_view(), name='api-task-complete'),

    path('api/story/', views.UserStoryList.as_view(), name='api-story-list'),
    path('api/story/<int:pk>/', views.UserStoryDetail.as_view(), name='api-story-detail'),
    path('api/story/<int:pk>/complete', views.UserStoryComplete.as_view(), name='api-story-complete'),


    
]

urlpatterns = format_suffix_patterns(urlpatterns)