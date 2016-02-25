# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_auto_20160225_0823'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='subject',
        ),
    ]
