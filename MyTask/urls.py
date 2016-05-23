from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'tasks.views.home', name='home'),
    url(r'^login/$', 'tasks.views.login', name='login'),
    url(r'^logout/$', 'tasks.views.logout', name='logout'),
    url(r'^clear/$', 'tasks.views.clear', name='clear'),
    url(r'^add/$', 'tasks.views.add_task', name='add_task'),
    url(r'^reg/$', 'tasks.views.reg', name='reg'),
    url(r'^success/$', 'tasks.views.success', name='success'),
    url(r'^error/$', 'tasks.views.error', name='error'),
    url(r'^check/([0-9]+)/$', 'tasks.views.check', name='check'),
    url(r'^uncheck/([0-9]+)/$', 'tasks.views.uncheck', name='uncheck'),
    url(r'^(.+)/$', 'tasks.views.home', name='register'),
)
