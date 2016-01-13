from django.db import models

# Create your models here.

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=1000)
    status = models.CharField(max_length=10, default='open')
    # user_id =
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)
