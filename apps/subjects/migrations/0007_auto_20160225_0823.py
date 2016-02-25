# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0006_usersubject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersubject',
            name='status',
            field=models.CharField(default='doing', choices=[('doing', 'Doing'), ('finish', 'Finish')], max_length=10),
        ),
    ]
