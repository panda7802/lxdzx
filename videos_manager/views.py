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
from django.http import StreamingHttpResponse

logger = logging.getLogger('sourceDns.webdns.views')


def t_index_view(req):
    res = render_to_response('index.html')
    logger.debug("-----------------")
    logger.error("-----------------")
    return res


def t_zl(req):
    url = "/home/ubuntu/projects/lxdzx/templates/apple-app-site-association"
    with open(url) as f:
        c = f.read()
    return HttpResponse(c, content_type='application/pkcs7-mime')


#   res = render_to_response('apple-app-site-association')
#   return res


def t_f(req):
    res = render_to_response('fileauth.htm')
    return res


def t_get_all_videos(req):
    start_id = int(req.GET.get('sid', 0))
    data_len = int(req.GET.get('len', 9999))
    t_id = int(req.GET.get('id', -1))

    tj_videos = []
    if t_id < 0:  # 没有id截取
        db_res = Videos.objects.order_by("-id")[start_id:(data_len + start_id)]
    else:
        db_res = Videos.objects.filter(id=t_id)  # .filter(id=t_id).filter(id__gte=t_id)

    for item in db_res:
        video = JVideos()
        video.id = item.id
        video.title = item.title  # 标题
        # logger.debug("----------------" + item.pic_url.url)
        # logger.debug("----------------" + TGlobalData.STATIC_RECV_PATH)
        if len(item.pic_url.url) > len(TGlobalData.STATIC_RECV_PATH):
            video.pic_url = item.pic_url.url[len(TGlobalData.STATIC_RECV_PATH):]  # 图片
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
