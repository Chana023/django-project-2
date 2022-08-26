from django.test import TestCase
from scrumapp.logic import *
from scrumapp.models import *
from factory.django import DjangoModelFactory
import factory

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

class TaskFactory(DjangoModelFactory):
    class Meta:
        model = Task

class UserStoryFactory(DjangoModelFactory):
    class Meta:
        model = User_Story


# Create your tests here.
class TestTask(TestCase):

    @classmethod
    def setUpTestData(cls):
        pass

    def setUp(self):
        developerforTestTask1 = UserFactory(username = 'devMan1234', password = 'somePassword')
        randomDev = UserFactory(username = 'randomDev', password = 'somePassword')
        user_story = UserStoryFactory()
        testTask1 = TaskFactory(name='TestTask1', developer=developerforTestTask1, user_story=user_story, status='N')

        user_story_all_task_completed = UserStoryFactory(name='story_tasks_completed')
        completeTask1 = TaskFactory(user_story=user_story_all_task_completed, status='C')
        completeTask2 = TaskFactory(user_story=user_story_all_task_completed, status='C')
        completeTask3 = TaskFactory(user_story=user_story_all_task_completed, status='C')

        user_story_incomplete_task = UserStoryFactory(name='story_tasks_incomplete')
        incompleteTask1 = TaskFactory(user_story=user_story_incomplete_task, status='N')
        incompleteTask2 = TaskFactory(user_story=user_story_incomplete_task, status='I')
        incompleteTask3 = TaskFactory(user_story=user_story_incomplete_task, status='C')
        

    def testIfAssignedDevCanCompleteTask(self):
        """
        Test if the user assigned to a task can complete a task
        """
        testTask1id = Task.objects.filter(name='TestTask1').values('id')[0].get('id')
        userid = User.objects.filter(username='devMan1234').values('id')[0].get('id')
        
        self.assertTrue(taskComplete(taskid=testTask1id, userid=userid))


    def test_if_not_assigned_dev_can_complete_task(self):
        """
        Test if a user not assigned to a task can complete a task
        """
        testTask1id = Task.objects.filter(name='TestTask1').values('id')[0].get('id')
        userid = User.objects.filter(username='randomDev').values('id')[0].get('id')
        self.assertFalse(taskComplete(taskid=testTask1id, userid=userid))


    def test_if_all_tasks_complete(self):
        """
        Check if when all tasks are completed the function 'is_tasks_complete' returns true
        """
        user_story_id_where_all_tasks_complete = User_Story.objects.filter(name='story_tasks_completed').values('id')[0].get('id')
        self.assertTrue(is_tasks_complete(user_story_id_where_all_tasks_complete))

    def test_if_there_is_an_incomplete_task_in_story(self):
        """
        Check if the is_task_complete function returns false if their is an incomplete task in a user story
        """
        user_story_id_where_all_tasks_complete = User_Story.objects.filter(name='story_tasks_incomplete').values('id')[0].get('id')
        self.assertFalse(is_tasks_complete(user_story_id_where_all_tasks_complete))

        
    


    


