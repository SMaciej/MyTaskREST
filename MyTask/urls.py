from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'tasks.views.home', name='home'),
    url(r'^logout/$', 'tasks.views.logout', name='logout'),
    url(r'^clear/$', 'tasks.views.clear', name='clear'),
    url(r'^check/([0-9]+)/$', 'tasks.views.check', name='check'),
    url(r'^uncheck/([0-9]+)/$', 'tasks.views.uncheck', name='uncheck'),
    url(r'^(.+)/$', 'tasks.views.home', name='register'),
)
