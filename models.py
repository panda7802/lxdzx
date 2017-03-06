# coding=utf-8

from __future__ import unicode_literals

from django.db import models
from tutils.tjson import TJsonTools
from tutils.t_global_data import TGlobalData
import django.utils.timezone as timezone


class Tags(models.Model):
    """
    标签
    """
    title = models.CharField('标题', max_length=128, default="", blank=True)  # 标题
    desc = models.CharField('说明', max_length=256, default="", blank=True)  # 说明
    bak_data = models.CharField('备用字段', max_length=1024, default="", blank=True)  # 备用字段

    def __unicode__(self):
        return self.title


class Videos(models.Model):
    """
    视频内容
    """
    title = models.CharField('标题', max_length=128, default="", blank=True)  # 标题
    pic_url = models.FileField('图片', upload_to=TGlobalData.STATIC_RECV_PATH) # 图片
    video_url = models.CharField('视频地址', max_length=1024, default="", blank=True)  # 视频地址
    desc = models.CharField('描述', max_length=1024, default="", blank=True)  # 描述
    tags = models.ManyToManyField(Tags)  # 标签
    upload_time = models.DateTimeField('保存日期', default=timezone.now) #时间
    keywords = models.CharField('关键字(用英文状态下逗号分隔)', max_length=1024, default="", blank=True)  # 关键字
    bak_data = models.CharField('备用字段', max_length=1024, default="", blank=True)  # 备用字段

    def __unicode__(self):
        return self.title

