# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-08 16:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20170508_1809'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='new_videou_url',
        ),
    ]