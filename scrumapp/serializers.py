from rest_framework import serializers
from scrumapp.models import Task

class TaskSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='api-task-detail', read_only=True)

    class Meta:
        model = Task
        fields = ['name', 'user_story', 'description','status','developer','completed_at','url'] 
        
