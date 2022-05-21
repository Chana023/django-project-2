from django.contrib import admin
from scrumapp.models import Task
from scrumapp.models import User
from scrumapp.models import User_Story

# Register your models here.
admin.site.register(Task)
admin.site.register(User_Story)
