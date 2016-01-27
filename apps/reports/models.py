from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Report(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    tags = models.ManyToManyField(User, related_name='tags', through='Tag')


class Tag(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    report = models.ForeignKey(Report, on_delete=models.CASCADE)

    class Meta:
        auto_created = True

