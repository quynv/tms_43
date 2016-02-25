# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0011_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercourse',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
