from django.shortcuts import render
from .models import Demo
from .serilizerclass import DemoSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django .http import HttpResponse
from django_ajax.decorators import ajax
from django.http import JsonResponse
import json


class MyClass(APIView):

    def get(self, request):
        print(request)
        obj = Demo.objects.all()
        serializer = DemoSerializer(obj, many=True)
        print(serializer.data)
        return Response(serializer.data)

    def post(self):
        pass


def index(request):
    context = {}
    return render(request, "ETSApp/index.html", context=context)


def home(request):
    context = {'my_key': "Welcome To AWS with Django"}
    return render(request, "ETSApp/home.html", context=context)


def database(request):
    obj = ""
    my_key = ""
    context = {}
    try:
        obj = Demo.objects.all()
        context = {'obj': obj, 'my_key': my_key}
    except:
        my_key = "Welcome To AWS with Django"
        context = {'my_key': my_key}

    return render(request, "ETSApp/database.html", context=context)


def ajax_test(request):
    print("}}}}}}}}}}}}}}}}}}}}}}}}")
    a = request.GET.get('name2')
    b = request.GET.get('mval')
    print(a, b)
    data = {'is_taken': 1, 'a': 2, 'b': 3, 'c': 4}
    # return HttpResponse(json.dumps(data), content_type='application/json')
    return JsonResponse(data)


def page(request):
    return render(request, 'ETSApp/ajaxtest.html', {})
