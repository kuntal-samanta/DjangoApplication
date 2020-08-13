from django.shortcuts import render
from .models import *
from django.db.models import Q
from datetime import datetime
import httpagentparser
import os
import sys


def GetRemotePCIP(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def BrowserDetails(request):
    agent = request.environ.get('HTTP_USER_AGENT')
    browser = httpagentparser.detect(agent)
    if not browser:
        browser = agent.split('/')[0]
    else:
        browser_name = browser['browser']['name'] 
        browser_version = browser['browser']['version']
        browser = browser_name + " " + browser_version
    return browser


def index(req):
    context = {'lst': ['Python' for i in range(10)]}
    return render(req, 'App/index.html', context=context)