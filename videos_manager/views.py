# coding=utf-8

from django.shortcuts import render

from django.http.response import HttpResponse
from django.shortcuts import render, render_to_response
import logging
from django.views.decorators.csrf import csrf_exempt
from tutils.t_global_data import TGlobalData

# Create your views here.
from models import Videos
from tutils import t_log
from tutils.tjson import TJsonTools
from TJsonModels import JVideos
import time
import datetime
import os


def t_index_view(req):
    res = render_to_response('index.html')
    return res


def t_get_all_videos(req):
    # res = render_to_response('index.html')
    db_res = Videos.objects.all()
    tj_videos = []
    for item in db_res:
        video = JVideos()
        video.title = item.title  # 标题
        video.pic_url = item.pic_url.url[len(TGlobalData.STATIC_FILE_PATH) + 2:]  # 图片
        video.video_url = item.video_url  # video_url;# 缩略图
        video.desc = item.desc  # 描述
        # video.tags = item.tags  # 标签
        video.upload_time = item.upload_time.strftime("%Y-%m-%d %H:%M")  # 时间
        video.keywords = item.keywords  # 关键字
        # video.bak_data = item.bak_data  # 备用字段
        tj_videos.append(video)
    logging.debug(TJsonTools.tJsonEncode(tj_videos).replace("},", '},' + os.linesep))
    res = HttpResponse(TJsonTools.tJsonEncode(tj_videos))
    return res
