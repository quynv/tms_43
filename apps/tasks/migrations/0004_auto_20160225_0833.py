# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20160224_1453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertask',
            name='status',
            field=models.CharField(default='doing', choices=[('doing', 'Doing'), ('finish', 'Finish')], max_length=10),
        ),
    ]
