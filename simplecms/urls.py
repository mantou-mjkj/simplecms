"""simplecms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
# from django.contrib import admin

urlpatterns = [
    # url(r'^admin/', include(admin.site.urls)),
    url(r'|^index/|^home/', include('home.urls')),
    url(r'^admin/article/', include('admin.article.urls')),
    url(r'^admin/user/', include('admin.user.urls')),
    url(r'^admin/cat/', include('admin.cat.urls')),
    url(r'^admin/detail/', include('admin.detail.urls')),
    url(r'^admin/test/',include('admin.testcms.urls'))
]
