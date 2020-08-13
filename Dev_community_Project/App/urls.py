from django.urls import path
from .import views

urlpatterns = [
    # path('', views., name=""),
    path('', views.index, name="home"),
]