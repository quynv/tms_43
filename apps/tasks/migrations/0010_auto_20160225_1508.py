# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0009_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='subject',
            field=models.ManyToManyField(to='subjects.Subject'),
        ),
    ]
