from django.db import models

from apps.subjects.models import Subject
from django.contrib.auth.models import User

status_choise = (
        ('doing', 'Doing'),
        ('finish', 'Finish'),
)

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50)
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    subject = models.ManyToManyField(Subject)


class UserTask(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,null=True,blank=True,related_name="users")
    task = models.ForeignKey(Task,null=True,blank=True,related_name="tasks")
    status = models.CharField(max_length=10, choices=status_choise, default='doing')
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
