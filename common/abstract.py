# -*- coding: UTF-8 -*-


class ViewComponent(object):
    name = ''

    def __init__(self):
        super(ViewComponent).__init__()
        if not self.slug:
            raise Exception("component should be implement!")

class Register(object):

    def __init__(self):
        self._register = {}


    def register(self, cls):
        if cls not in self._register:
            self._register[cls] = cls()
        return self._register

class AbstractView(ViewComponent):
    name = ''
    slug = ''

    def autodiscover(self):
        pass

    @staticmethod
    def register(cls):
        register.register(cls)


register = Register()