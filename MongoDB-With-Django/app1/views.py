from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Student


def home(request):
    print(request)
    obj = Student.objects.all()
    for i in obj:
        print(i.id, i.name, "\n", i.desc)
    return HttpResponse("<h2> Hello Mongo DB</h2>")

