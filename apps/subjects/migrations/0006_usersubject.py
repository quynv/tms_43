# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-24 10:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subjects', '0005_auto_20160218_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSubject',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[(b'doing', b'Doing'), (b'finish', b'Finish')], default=b'doing', max_length=10)),
                ('updated_at', models.DateField(auto_now=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('subject', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='subjects.Subject')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_subjects', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
