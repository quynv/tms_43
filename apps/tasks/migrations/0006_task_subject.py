# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0009_remove_subject_task'),
        ('tasks', '0005_remove_task_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='subject',
            field=models.ManyToManyField(to='subjects.Subject'),
        ),
    ]
