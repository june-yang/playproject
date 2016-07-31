#-*- coding: UTF-8 -*-
import io
import os

import django
from django.conf import settings
from django.template.base import TemplateDoesNotExist  # noqa

if django.get_version() >= '1.8':
    from django.template.engine import Engine
    from django.template.loaders.base import Loader as tLoaderCls
else:
    from django.template.loader import BaseLoader as tLoaderCls  # noqa

from django.utils._os import safe_join  # noqa
from os.path import join,dirname,abspath

# sub-app templates load to itself dir rather it's father templates dir
class TemplateLoader(tLoaderCls):
    is_usable = True

    def get_template_sources(self, template_name):
        PROJECT_DIR = dirname(dirname(abspath(__file__)))
        bits = template_name.split('/')
        if len(bits) == 2:
            sub_app, remainder = bits
            template_dir = '%s/kanban/%s/templates'% (PROJECT_DIR, sub_app,)
            try:
                yield safe_join(template_dir, remainder)
            except UnicodeDecodeError:
                # The template dir name wasn't valid UTF-8.
                raise
            except ValueError:
                # The joined path was located outside of template_dir.
                pass
        if len(bits) == 3:
            sub_app, view_group, remainder = bits
            template_dir = '%s/kanban/%s/%s/templates'% (PROJECT_DIR, sub_app, view_group)
            try:
                yield safe_join(template_dir, remainder)
            except UnicodeDecodeError:
                # The template dir name wasn't valid UTF-8.
                raise
            except ValueError:
                # The joined path was located outside of template_dir.
                pass

    def load_template_source(self, template_name, template_dirs=None):
        for path in self.get_template_sources(template_name):
            try:
                with io.open(path, encoding=settings.FILE_CHARSET) as file:
                    return (file.read(), path)
            except IOError:
                pass
        raise TemplateDoesNotExist(template_name)


if django.get_version() >= '1.8':
    e = Engine()
    _loader = TemplateLoader(e)
else:
    _loader = TemplateLoader()
