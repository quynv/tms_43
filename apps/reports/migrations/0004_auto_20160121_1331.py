# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0003_auto_20160114_0824'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='report',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='user',
        ),
        migrations.AlterField(
            model_name='report',
            name='tags',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name='tags'),
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
    ]
