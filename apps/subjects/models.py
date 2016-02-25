from django.db import models

from apps.courses.models import Course
from django.contrib.auth.models import User

status_choise = (
        ('open', 'Opening'),
        ('close', 'Closed'),
)

user_subject_status = (
        ('doing', 'Doing'),
        ('finish', 'Finish'),
)

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=status_choise, default='open')
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    course = models.ManyToManyField(Course)


class UserSubject(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,null=True,blank=True,related_name="user_subjects")
    subject = models.ForeignKey(Subject,null=True,blank=True,related_name="subjects")
    status = models.CharField(max_length=10, choices=user_subject_status, default='doing')
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
