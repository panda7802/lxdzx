# coding=utf-8


class JVideos:
    """
    视频内容
    """
    def __init__(self):
        pass
        # title # 标题
        # pic_url; # 图片
        # video_url;# 缩略图
        # desc = models.CharField('描述', max_length=1024, default="", blank=True)  # 描述
        # tags = models.ManyToManyField(Tags)  # 标签
        # upload_time = models.DateTimeField('保存日期', default=timezone.now) #时间
        # keywords = models.CharField('关键字(用英文状态下逗号分隔)', max_length=1024, default="", blank=True)  # 关键字
        # bak_data = models.CharField('备用字段', max_length=1024, default="", blank=True)  # 备用字段
