'''
        views.py
   @ Author  Kuntal
   @ Company 
   @ version  0.1
   @date      10/12/2019
'''
# Django Import
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth import authenticate
from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse, Http404
import datetime
import json
from django.contrib import messages
from BlankSetup import settings
DEFAUT_IMAGE = settings.DEFAULT_IMAGE_PATH

# Cache Import
from django.core.cache import cache

# Model Import
from App import models

# Serializers Import
from App import serializers

# Rest Framework
'''from rest_framework.views import APIView'''
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
'''from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework import authentication, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions'''

# Import Help Packages
from App.help import browserDetect, emailHelp, IPdetect, JWTEncodeDecode, numberGenerator, \
    SHAEncodeDecode


@api_view(['GET'])
def Test(request):
    '''users = User.objects.all().select_related('profile')'''

    '''messages.add_message(request, messages.INFO, 'Student created successfully1')
    messages.success(request, 'Student created successfully2')
    messages.info(request, 'Student created successfully3')
    messages.warning(request, 'Student created successfully4')'''

    '''obj = get_object_or_404(MyModel, pk=1)'''

    return render(request, 'App/home.html', context={})