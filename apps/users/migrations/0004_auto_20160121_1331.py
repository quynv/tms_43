# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import apps.users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_userprofile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(max_length=257, default='', upload_to=apps.users.models._path_to_avatar, blank=True),
        ),
    ]
