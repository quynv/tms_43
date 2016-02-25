# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_task_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='subject',
            field=models.ManyToManyField(related_name='task', to='subjects.Subject'),
        ),
    ]
