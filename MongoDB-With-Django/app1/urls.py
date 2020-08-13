from django.conf.urls import url
from .import views


urlpatterns = [
    # url(r'^/$', views.function_name, name="Page")

    url(r'^$', views.home, name="Home Page"),
]

