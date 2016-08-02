# -*- coding: UTF-8 -*-
from common.abstract import AbstractView
from common.abstract import ViewComponent

class IndexView(ViewComponent):
    name = 'index'
    slug = 'index/'

AbstractView.register(IndexView)