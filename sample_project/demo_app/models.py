from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify 
from django.urls import reverse
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver


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


class MyBlog(models.Model): 
    title = models.CharField(max_length = 10) 
    slug = models.SlugField() 
  
    def save(self, *args, **kwargs): 
        self.slug = slugify(self.title) 
        super(MyBlog, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("sample_slugify_blog_url", kwargs={"slug": self.slug})


"""class Blog(models.Model):
    blogId = models.TextField()
    blogHeading = models.TextField()
    blogContent = models.TextField()
    blogImage = models.ImageField(upload_to='BlogImage/')
    blogCreatorName = models.TextField()
    blogCreatorMail = models.EmailField()
    blogCreatorImage = models.ImageField(upload_to='BlogerImage/')
    blogLikedBy = models.ListField(default=[])
    blogDisLikeBy = models.ListField(default=[])
    blogComment = models.ListField(default={})
    blogLikeCount = models.IntegerField()
    blogDisLikeCount = models.IntegerField()
    blogPostTime = models.DateTimeField()"""




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


