# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-15 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos_manager', '0004_auto_20170215_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='pic_url',
            field=models.FileField(upload_to='F:\\pythonCode\\lxdzx/static/files//recv/'),
        ),
    ]