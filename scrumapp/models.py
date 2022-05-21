from django.db import models

# Create your models here.


# class for managing user model
class User(models.Model):
    ROLE_CHOICES = [
        ('SM', 'Scrum_Master'),
        ('D', 'Developer'),
    ]
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    role = models.CharField(max_length=2, choices=ROLE_CHOICES, default='D')


#class for managing User story model
class User_Story(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    last_update = models.DateTimeField(auto_now=True)


#class for managing the task model
class Task(models.Model):
    STATUS_CHOICES = [
        ('N', 'NEW'),
        ('I', 'IN_PROGRESS'),
        ('C', 'COMPLETE'),
    ]
    name = models.CharField(max_length=255)
    user_story = models.ForeignKey(User_Story, on_delete=models.CASCADE)
    description = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES,default='N')
    
