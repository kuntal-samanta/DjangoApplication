# Django Import
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
from django.contrib import messages
from django.shortcuts import render
from django.template import loader
from django.template.loader import render_to_string

# settings proparty
from django.conf import settings

# cache import
from django.core.cache import cache

# common import
import datetime
import json

# default image
DEFAUT_IMAGE = settings.DEFAULT_IMAGE_PATH

# model import
from demo_app import models


def Test(request):
    return HttpResponse("Hello World from app1")


def sample_html_1(request):
    context={
        'key': "Kuntal-app1",
        'rand_num': [10, 20, 30, 40]
    }
    template = loader.get_template('app1/test.html')
    template = template.render(context)
    return HttpResponse(template)


def sample_html_2(request):
    context={
        'key': "Kuntal-app1-2",
        'rand_num': [100, 200, 300, 400]
    }
    return render(request, 'app1/test.html', context=context)


def sample_html_3(request):
    context={
        'key': "Kuntal-app1-3",
        'rand_num': [101, 201, 301, 401]
    }
    rendered = render_to_string('app1/test.html', context=context)
    return HttpResponse(rendered)
    

def sample_html_4(request):
    return render(request, 'app2/test.html', context={})

