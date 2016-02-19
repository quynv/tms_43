# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('report', models.ForeignKey(to='reports.Report')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, default=0)),
            ],
        ),
        migrations.AddField(
            model_name='report',
            name='tags',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, through='reports.Tag', related_name='tags'),
        ),
        migrations.AddField(
            model_name='report',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, default=0),
        ),
    ]
