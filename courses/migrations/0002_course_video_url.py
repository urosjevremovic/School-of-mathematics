# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-08 14:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='video_url',
            field=models.TextField(default='s'),
            preserve_default=False,
        ),
    ]