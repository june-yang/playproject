# -*- coding: UTF-8 -*-
from django.conf.urls import url
from django.conf.urls import include
from django.conf.urls import patterns

class ViewComponent(object):
    default_index_name = ''

    def __init__(self):
        if not self.slug:
            raise Exception("component should be implement!")

class Register(object):

    def __init__(self):
        self._register = {}


    def register(self, cls):
        if cls not in self._register:
            self._register[cls] = cls()
        return self._register

class AbstractView():
    name = ''
    slug = ''
    register = {}

    def autodiscover(self):
        urlpatterns = []
        import pdb
        pdb.set_trace()
        for view in self.register:
            urlpatterns += patterns('', url(r'^' + view.slug + '$', 'kanban.%s.urls'%view.default_index_name))
        return urlpatterns

    def register(self, cls):
        if cls not in self.register:
            self.register[cls] = cls()
        return self.register
