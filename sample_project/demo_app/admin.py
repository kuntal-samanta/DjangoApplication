from django.contrib import admin
from .models import Car, SecureFiles, MyBlog


admin.site.register(Car)
admin.site.register(SecureFiles)
admin.site.register(MyBlog)
