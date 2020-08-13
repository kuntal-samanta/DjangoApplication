from django.db import models
from django.contrib.auth.models import User


class UserDetails(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    profile_photo = models.ImageField(upload_to='User/Profile/Image/', blank=True, null=True)
    phone = models.CharField(max_length=10, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    dob = models.DateField(auto_now=False, blank=True, null=True)


class Post(models.Model):
    heading = models.CharField(max_length=250)
    body = models.TextField()
    tag = models.CharField(max_length=20, blank=True, null=True)
    image = models.ImageField(upload_to='User/Post/Image/', blank=True, null=True)
    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    create_at = models.DateTimeField(auto_now_add=True)


class Tags(models.Model):
    tag = models.CharField(max_length=20, blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)