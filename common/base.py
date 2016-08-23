# -*- coding: utf-8 -*-
from common.abstract import AbstractView


def url():
    return AbstractView().autodiscover()
