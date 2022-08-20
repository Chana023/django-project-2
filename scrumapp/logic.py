from datetime import datetime
from rest_framework.exceptions import PermissionDenied
from scrumapp.models import Task, User, User_Story
from rest_framework import status
from rest_framework.response import Response

#Logic functions

def taskComplete(taskid, userid):
        
        if(userid == Task.objects.filter(id=taskid).values('developer_id')[0].get('developer_id')):
                task = Task.objects.filter(id=taskid).update(status='C')
                task = Task.objects.filter(id=taskid).update(completed_at=datetime.now())
                return Response(status=status.HTTP_200_OK)
        else:
                return Response(status=status.HTTP_401_UNAUTHORIZED)

def is_tasks_complete(userstoryid):
        task_statuses = Task.objects.filter(user_story=userstoryid).values('status')
        for status in task_statuses:
                if status['status'] != 'C':
                        return False
        return True

def story_complete(userstoryid, userid):
        if is_tasks_complete(userstoryid=userstoryid) == True:
                return Response(status=status.HTTP_200_OK)
        else:
                return Response({'tasks for user story are not complete'},status=status.HTTP_400_BAD_REQUEST)
        

        