from djongo import models


class Student(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()
    img = models.ImageField(upload_to='Image')
    created_on = models.DateTimeField(auto_now_add=True)


class Post(models.Model):
    name = models.CharField(max_length=20)
    tag = models.ListField()


class Dmo(models.Model):
    name = models.CharField(max_length=20)
    no = models.IntegerField()
