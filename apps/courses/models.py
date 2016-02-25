from django.db import models
from django.contrib.auth.models import User

status_choise = (
        ('open', 'Opening'),
        ('close', 'Closed'),
)


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    status = models.CharField(max_length=10, choices=status_choise, default='open')
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    supervisors = models.ManyToManyField(User, blank=True)


class UserCourse(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User,null=True,blank=True,related_name="user_courses")
    course = models.ForeignKey(Course,null=True,blank=True,related_name="courses")
    is_active = models.BooleanField(default=False)
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
