from datetime import datetime
from rest_framework.exceptions import PermissionDenied
from scrumapp.models import Task, User, User_Story
from rest_framework import status
from rest_framework.response import Response

#Logic functions

def taskComplete(taskid, userid):
        
        if(userid == Task.objects.filter(id=taskid).values('developer_id')[0].get('developer_id')):
                Task.objects.filter(id=taskid).update(status='C')
                Task.objects.filter(id=taskid).update(completed_at=datetime.now())
                return True
        else:
                return False

def is_tasks_complete(userstoryid):
        task_statuses = Task.objects.filter(user_story=userstoryid).values('status')
        for status in task_statuses:
                if status['status'] != 'C':
                        return False
        return True

def story_complete(userstoryid, userid):
        if is_tasks_complete(userstoryid=userstoryid) == True:
                User_Story.objects.filter(id=userstoryid).update(completed_at=datetime.now())
                User_Story.objects.filter(id=userstoryid).update(completed_by=userid)
                return True
        else:
                return False
        

        