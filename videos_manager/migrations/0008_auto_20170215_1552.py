# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-15 07:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos_manager', '0007_auto_20170215_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='video_url',
            field=models.CharField(blank=True, default='', max_length=128, verbose_name='\u89c6\u9891\u5730\u5740'),
        ),
    ]
