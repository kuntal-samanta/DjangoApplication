'''
        urls.py
   @ Author  Kuntal
   @ Company 
   @ version  0.1
   @date      10/12/2019
'''

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('superadmin/', admin.site.urls),
    path('app/', include('App.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)