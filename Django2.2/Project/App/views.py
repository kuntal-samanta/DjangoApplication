from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
import datetime
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password


