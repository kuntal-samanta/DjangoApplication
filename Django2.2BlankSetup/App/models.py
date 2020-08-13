# https://docs.djangoproject.com/en/3.0/ref/contrib/auth/
'''
        models.py
   @ Author  Kuntal
   @ Company 
   @ version  0.1
   @date      10/12/2019
'''

from django.db import models
from django.utils.text import slugify        # <-- importing slugify from django   
from BlankSetup import settings
DEFAUT_IMAGE = settings.DEFAULT_IMAGE_PATH
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver

  
# Create your models here. 
class GeeksModel(models.Model): 
    title = models.CharField(max_length = 200) 
    slug = models.SlugField() 
  
    def save(self, *args, **kwargs): 
        self.slug = slugify(self.title) 
        super(GeeksModel, self).save(*args, **kwargs) 



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()