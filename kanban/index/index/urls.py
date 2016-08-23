# -*- coding: UTF-8 -*-
from django.conf.urls import url
from django.conf.urls import patterns

urlpatterns = patterns(
    'kanban.index.index.views',
    url('^$', 'index'),
)