from datetime import datetime
from rest_framework.exceptions import PermissionDenied
from scrumapp.models import Task, User, User_Story
from rest_framework import status
from rest_framework.response import Response

#Logic functions

def is_developer(user):
    return user.groups.filter(name='Developer').exists()

def is_scrum_master(user):
    return user.groups.filter(name='Scrum Master').exists()

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
        user = User.objects.filter(id=userid)[0]
        print()
        if is_tasks_complete(userstoryid=userstoryid) == True and is_scrum_master(user) == True:
                User_Story.objects.filter(id=userstoryid).update(completed_at=datetime.now())
                User_Story.objects.filter(id=userstoryid).update(completed_by=userid)
                return True
        else:
                return False


def is_user_allowed_to_update_Task(task_id, user_id):
        """
        Checks if a user is a Scrum Master or Developer who is allowed to update a given task. 
        Scrum Masters can update any Task
        Developers can only update tasks assigned to them.
        """

        task = Task.objects.filter(id=task_id)[0]
        user = User.objects.filter(id=user_id)[0]
        
        if user.groups.filter(name='Developer') and task.developer.id == user_id:
                return True
        elif user.groups.filter(name='Scrum Master'):
            return True
        else:
            raise False

def get_user_story_list(user_id):
        user = User.objects.filter(id=user_id)[0]
        list_of_tasks_for_user = []

        if user.groups.filter(name='Developer'):
                tasks_for_developer = Task.objects.filter(developer=user)
                for task in tasks_for_developer:
                        list_of_tasks_for_user.append(task.user_story.id)
                set_of_story_id_for_user = set(list_of_tasks_for_user)
                print(set_of_story_id_for_user)
                return User_Story.objects.filter(id__in=set_of_story_id_for_user)
        elif user.groups.filter(name='Scrum Master'):
                return User_Story.objects.all()

        