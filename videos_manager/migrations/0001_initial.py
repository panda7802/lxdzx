# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-15 06:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=128)),
                ('pic_url', models.CharField(default='', max_length=512)),
                ('video_url', models.CharField(default='', max_length=128)),
                ('desc', models.CharField(default='', max_length=1024)),
                ('keywords', models.CharField(default='', max_length=1024)),
                ('bak_data', models.CharField(default='', max_length=1024)),
                ('tags', models.ManyToManyField(to='videos_manager.Tags')),
            ],
        ),
    ]
