# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-28 06:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos_manager', '0009_auto_20170228_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='pic_url',
            field=models.FileField(upload_to='F:\\pythonCode\\lxdzx/static/files//recv/', verbose_name='\u56fe\u7247'),
        ),
    ]
