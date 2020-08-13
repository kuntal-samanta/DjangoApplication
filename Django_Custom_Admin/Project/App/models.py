from __future__ import unicode_literals
# from django.core.urlresolvers import reverse
from django.db import models
from django.contrib.auth.models import User


# One To One
class UserDetails(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    phone = models.CharField(max_length=10, blank=True, null=True)
    
    def __str__(self):
        return self.phone
    
    class Meta:
        db_table = "UserDetails"
        ordering = ['phone']
    


# ForeignKey
class Batch(models.Model):
    batch_id = models.CharField(max_length=10)
    batch_name = models.CharField(max_length=50)
    

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    batch = models.ForeignKey(
            Batch,
            on_delete=models.CASCADE,
            related_name="batch_allocating",
            blank=True,
            null=True
        )


# Many To Many
class Course(models.Model):
    name = models.TextField()
    year = models.IntegerField()

    class Meta:
        unique_together = ["name", "year"]
    
    def __str__(self):
        return self.name
    

class Person(models.Model):
    last_name = models.TextField()
    first_name = models.TextField()
    courses = models.ManyToManyField("Course")

    class Meta:
        verbose_name_plural = "People"



# ForeignKey and ManyToManyField --> Through Key
class Person_More(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Group_More(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person_More, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person_More, on_delete=models.CASCADE)
    group = models.ForeignKey(Group_More, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)



# Admin Custom
class Product(models.Model):
    title = models.CharField(
        max_length=10,
        help_text="Enter Product Name"
    )
    description = models.TextField(help_text="Type Description")
    price = models.FloatField(help_text="Price Of Product")
    is_active = models.BooleanField(default=True)
    
    # def get_absolute_url(self):
    #     return reverse("model_detail", kwargs={"pk": self.pk})