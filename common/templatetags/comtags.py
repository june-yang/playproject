# -*- coding:utf-8 -*-
from django import template
from django.conf import settings

register = template.Library()

@register.inclusion_tag('_base_script.html', takes_context=True)
def baseScript(context):
    STATIC_URL = settings.STATIC_URL
    return {'STATIC_URL': STATIC_URL}