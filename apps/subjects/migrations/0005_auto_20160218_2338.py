# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0004_auto_20160218_0843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='status',
            field=models.CharField(max_length=10, choices=[('open', 'Opening'), ('close', 'Closed')], default='open'),
        ),
    ]
