# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_remove_task_subject'),
        ('subjects', '0007_auto_20160225_0823'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='task',
            field=models.ManyToManyField(to='tasks.Task', related_name='task'),
        ),
    ]
