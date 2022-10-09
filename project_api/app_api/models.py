from django.db import models
from django.contrib.auth.models import User


# class UserTag(models.Model):
#     tag_name = models.CharField(max_length=10, default='')
#     created_at = models.DateField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.tag_name}'


# class UserProfile(models.Model):
#     user = models.OneToOneField(
#         User,
#         primary_key=True,
#         on_delete=models.CASCADE
#     )
#     gender = models.CharField(max_length=1, default='')
#     phone = models.CharField(max_length=10, default='')
#     profile_image = models.ImageField(
#         upload_to='User/Proile_Image', 
#         blank=True, null=True,
#         help_text="Profile Image"
#     )
#     tag = models.ManyToManyField(UserTag)

#     def __str__(self):
#         return f'UserProfile for {self.user.username}'



class School(models.Model):
    school_name = models.CharField(max_length=20, default='School', help_text="School Name")

    def __str__(self):
        return f'{self.school_name}'


class Standerd(models.Model):
    standerd_name = models.CharField(max_length=5, default='STD 1', help_text="Class Name")
    school = models.ForeignKey(
        School,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.school.school_name} - {self.standerd_name}'


class Tag(models.Model):
    tag_name = models.CharField(max_length=10, default='')
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.tag_name}'


class Author(models.Model):
    author_name = models.CharField(max_length=10, default='Author')
    author_email = models.EmailField(default='', help_text='author email [author@email.com]')

    def __str__(self):
        return f'Author - {self.author_name}'


class Book(models.Model):
    book_name = models.CharField(max_length=10, default='Book')
    book_page = models.PositiveSmallIntegerField(default=1)
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )
    tag = models.ManyToManyField(Tag)
    for_standerd = models.ForeignKey(
        Standerd,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'Book - {self.book_name}'




