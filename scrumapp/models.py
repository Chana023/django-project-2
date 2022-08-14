from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


# class for managing user model
class User(AbstractUser):
    ROLE_CHOICES = [
        ('SM', 'Scrum_Master'),
        ('D', 'Developer'),
    ]
    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default='D')


#class for managing User story model
class User_Story(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    last_update = models.DateTimeField(auto_now=True)
    scrum_master = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    completed_at = models.DateTimeField(default=None, blank=True, null=True)
    completed_by = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, blank=True, null=True, related_name='completed_by')

    def __str__(self):
        return self.name

#class for managing the task model
class Task(models.Model):
    STATUS_CHOICES = [
        ('N', 'NEW'),
        ('I', 'IN_PROGRESS'),
        ('C', 'COMPLETE'),
    ]
    name = models.CharField(max_length=255)
    user_story = models.ForeignKey(User_Story, on_delete=models.CASCADE, related_name='task')
    description = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,default='N')
    developer = models.ForeignKey(User, on_delete=models.SET_NULL, default=None, blank=True, null=True)
    completed_at = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name
    
