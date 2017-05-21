# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-12 12:06
from __future__ import unicode_literals

from django.db import migrations
import embed_video.fields


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_step'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='video_url',
        ),
        migrations.AddField(
            model_name='step',
            name='video_url',
            field=embed_video.fields.EmbedVideoField(default=' '),
            preserve_default=False,
        ),
    ]