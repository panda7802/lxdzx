from django.contrib import admin

from videos_manager.models import Tags
from videos_manager.models import Videos

# Register your models here.
admin.site.register(Tags)
admin.site.register(Videos)

