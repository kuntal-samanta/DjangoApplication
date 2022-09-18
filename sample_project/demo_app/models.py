from django.db import models


'''
the following code will store uploaded files under /media/photos 
regardless of what your MEDIA_ROOT setting is

from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location='/media/photos')

class Example_Media(models.Model):
    photo = models.ImageField(storage=fs)
'''


class Car(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    photo = models.ImageField(upload_to='cars')
    specs = models.FileField(upload_to='specs')


class SecureFiles(models.Model):
    name = models.CharField(max_length=255)
    photo1 = models.ImageField(upload_to='secure')
    photo2 = models.ImageField(upload_to='open')


