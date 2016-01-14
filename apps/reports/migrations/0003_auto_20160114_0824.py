# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reports', '0002_auto_20160113_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='report',
            name='users',
        ),
        migrations.AddField(
            model_name='report',
            name='user',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='report',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='report',
            field=models.ForeignKey(to='reports.Report'),
        ),
        migrations.AddField(
            model_name='tag',
            name='user',
            field=models.ForeignKey(default=0, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='report',
            name='tags',
            field=models.ManyToManyField(through='reports.Tag', to=settings.AUTH_USER_MODEL, related_name='tags'),
        ),
    ]
