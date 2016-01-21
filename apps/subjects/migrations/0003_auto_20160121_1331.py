# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_auto_20160114_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='status',
            field=models.CharField(max_length=10, default='open'),
        ),
    ]
