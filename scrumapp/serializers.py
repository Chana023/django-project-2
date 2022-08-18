from rest_framework import serializers
from scrumapp.models import Task, User_Story

class TaskSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api-task-detail', read_only=True)

    class Meta:
        model = Task
        fields = ['id','name', 'user_story', 'description','status','developer','completed_at','url',] 

class TaskCompleteSerializer(serializers.ModelSerializer):
        class Meta:
            model = Task
            fields = ['name','status','completed_at','developer'] 


class UserStorySerializier(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api-story-detail', read_only=True)
    task = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = User_Story
        fields = ['id','name', 'description', 'last_update', 'scrum_master', 'completed_at',
         'completed_by', 'url', 'task',]

