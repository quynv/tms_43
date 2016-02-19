# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20160203_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='status',
            field=models.CharField(max_length=10, choices=[('open', 'Opening'), ('close', 'Closed')], default='open'),
        ),
    ]
