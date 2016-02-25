# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0008_subject_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='task',
        ),
    ]
