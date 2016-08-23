# -*- coding: UTF-8 -*-
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def index(request):
    return render_to_response('index/index/index.html', {'site_branding': '首页'})