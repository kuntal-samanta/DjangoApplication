# django
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import Q
from .models import *
from .serializers import *
from django.core.cache import cache #cache
# rest_framework
from rest_framework import generics
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

from .models import *



def Test(request):
    return HttpResponse("Health Ok")



# Test API
class UserListAPIView(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    queryset = User.objects.all()
    serializer_class = All_User_Serializer
    '''
        curl --location --request GET 'http://127.0.0.1:8000/users/'
    '''





class Book_List_API_View_1(generics.ListAPIView):
    permission_classes = [AllowAny, ]
    parser_classes = [JSONParser]
    queryset = Book.objects.all()
    serializer_class = All_Book_Serializer
    '''
        curl --location --request GET 'http://127.0.0.1:8000/1/books/'
    '''


class Book_List_API_View_2(APIView):
    permission_classes = [AllowAny, ]

    def get(self, request, format=None):
        queryset = Book.objects.all()
        serializer = All_Book_Serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    '''
        curl --location --request GET 'http://127.0.0.1:8000/2/books/'
    '''

    # def put(self, request, format=None):
    #     queryset = Book.objects.get(id=1)
    #     serializer = All_Book_Serializer(queryset, request.data, partial=True)
    #     if serializer.is_valid():
    #         serializer.save()     
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    # def post(self, request, format=None):
    #     name = request.data['name']
    #     email = request.data['email']
    #     print(name, email)
    #     serializer = All_Book_Serializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)




class Book_Create_API_View(generics.CreateAPIView):
    permission_classes = [AllowAny, ]
    queryset = Book.objects.all()
    serializer_class = All_Book_Serializer








