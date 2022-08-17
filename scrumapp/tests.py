from urllib import response
from django.test import TestCase
from .logic import *
from scrumapp.models import *
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status
from rest_framework import request


# Create your tests here.
class TestTaskUpdate(TestCase):

    def test_task_complete_logic(self):
        testdata = {
            "name": "Task task",
            "status": "I",
            "completed_at": None,
            "developer": 1
        }
        taskComplete(self, testdata, requestuser=1)
        self.assertEqual(testdata.get('status'),'C')


        
    


    


