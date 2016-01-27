# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import apps.users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_document'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='avatar',
            field=models.FileField(upload_to=apps.users.models._path_to_avatar, max_length=257, default='', blank=True),
        ),
    ]
