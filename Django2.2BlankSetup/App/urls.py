'''
        App.urls.py
   @ Author  Kuntal
   @ Company 
   @ version  0.1
   @date      10/12/2019
'''

from django.urls import path
from .import views


urlpatterns = [
    path('test/', views.Test, name="test"),
    # path('test/<int:num1>/<int:num2>', views.Test, name="test"),
]