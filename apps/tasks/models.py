from django.db import models

from apps.subjects.models import Subject

status_choise = (
        ('doing', 'Doing'),
        ('finish', 'Finish'),
)

class Task(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=25)
    description = models.CharField(max_length=50)
    status = models.CharField(max_length=10, choices=status_choise, default='doing')
    # user_id =
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
    subject = models.ManyToManyField(Subject)
