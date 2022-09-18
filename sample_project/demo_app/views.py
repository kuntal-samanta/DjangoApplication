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
from django.contrib.auth.decorators import login_required
from django.http import FileResponse

# settings proparty
from django.conf import settings

# cache import
from django.core.cache import cache

# common import
import datetime
import json
import os

# default image
DEFAUT_IMAGE = settings.DEFAULT_IMAGE_PATH

# model import
from demo_app import models


def Test(request):
    return HttpResponse("Hello World from app1")


#################################### Template ####################################
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
    rendered = render_to_string('app2/test.html', context=context)
    return HttpResponse(rendered)
    

def sample_html_4(request):
    return render(request, 'app2/test.html', context={})
#################################### Template ####################################




############################ Media Files & Access Control ############################
def test_media(request):
    context = {
        'car_object': models.Car.objects.get(id=1),
        'img_obj': models.SecureFiles.objects.get(id=1)
    }
    return render(request, 'app3/az.html', context=context)


@login_required # only if has owner permission
def secure(request,file):
    document = get_object_or_404(models.SecureFiles, name='Test1').photo1
    response = FileResponse(document)
    return response


# Create a Python file object using open() and the with statement
def sample_working_with_files():
    from django.core.files import File

    with open('/path/to/hello.world', 'w') as f:
        myfile = File(f)
        myfile.write('Hello World')
        myfile.closed
############################ Media Files & Access Control ############################


############################ slugify instead of id ############################
def test_slugify(request):
    context = {
        'all_blog': models.MyBlog.objects.all()
    }
    return render(request, 'app4/all_blog.html', context=context)


def test_slugify_special_blog(request, slug):
    print("#"*10, slug)
    context = {
        'one_blog': models.MyBlog.objects.get(slug=slug)
    }
    return render(request, 'app4/single.html', context=context)
############################ slugify instead of id ############################






