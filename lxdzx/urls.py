"""lxdzx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from lxdzx import settings
import videos_manager.views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', videos_manager.views.t_index_view),
    url(r'^get_all_videos$', videos_manager.views.t_get_all_videos),
    url(r'.well-known/pki-validation/fileauth.htm', videos_manager.views.t_f),
    url(r'apple-app-site-association', videos_manager.views.t_zl),
	#url(r'h.htm', videos_manager.views.t_f),
    #url(r'.well-known/pki-validation/fileauth.htm', videos_manager.views.t_index_view),
]


