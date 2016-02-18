from django.db import models

from apps.courses.models import Course

status_choise = (
        ('open', 'Opening'),
        ('close', 'Closed'),
)

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=status_choise, default='open')
    # user_id =
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    course = models.ManyToManyField(Course)
