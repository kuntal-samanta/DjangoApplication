from turtle import title
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify 
from django.urls import reverse
from django.db.models.signals import post_save, pre_save, pre_delete
from django.dispatch import receiver
from django.core.validators import MinValueValidator, MaxValueValidator


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


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
 
    def __str__(self):
        return f'{self.user.username} Profile'


class MyBlog(models.Model): 
    title = models.CharField(max_length = 10) 
    slug = models.SlugField() 
    
    # save overrite
    def save(self, *args, **kwargs): 
        self.slug = slugify(self.title) 
        super(MyBlog, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
        return reverse("sample_slugify_blog_url", kwargs={"slug": self.slug})
    
    # def get_absolute_url(self):
    #     return "/people/%i/" % self.id



"""
    Add a classmethod on the model class

class Book(models.Model):
    title = models.CharField(max_length=100)

    @classmethod
    def create(cls, title):
        book = cls(title=title)
        # do something with the book
        return book

book = Book.create("Pride and Prejudice")

obj, created = Person.objects.get_or_create(
    first_name='John',
    last_name='Lennon',
    defaults={'birthday': date(1940, 10, 9)},
)
"""


"""
    Add a method on a custom manager (usually preferred)

class BookManager(models.Manager):
    def create_book(self, title):
        book = self.create(title=title)
        return book
    
    def my_filter(self, name):
        return Book.objects.filter(title=name)


class Book(models.Model):
    title = models.CharField(max_length=100)
    book_create_manager = BookManager()
    objects = models.Manager()

>> Book.objects.create_book("Pride and Prejudice")    
>> Book.book_create_manager.my_filter(name="Book5")




class DahlBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(author='Roald Dahl')

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    # The default manager.
    objects = models.Manager()
    # The Dahl-specific manager
    dahl_objects = DahlBookManager()



class AuthorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role='A')

class EditorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(role='E')

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=1, choices=[('A', _('Author')), ('E', _('Editor'))])
    people = models.Manager()
    authors = AuthorManager()
    editors = EditorManager()
"""

# Exaple of Custom manager
class BookManager(models.Manager):
    def create_book(self, title):
        book = self.create(title=title)
        return book
    
    def my_filter(self, name):
        return Book.objects.filter(title=name)


class Book(models.Model):
    title = models.CharField(max_length=100)
    book_create_manager = BookManager()
    objects = models.Manager()






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
        # verbose_name="related place",
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
            null=True,
            # verbose_name="related place",
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



"""
    Abstract base classes

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

"""


"""
    Proxy Model

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

class MyPerson(Person):
    class Meta:
        proxy = True

    def do_something(self):
        # ...
        pass

>>> p = Person.objects.create(first_name="foobar")
>>> MyPerson.objects.get(first_name="foobar")
"""


"""
    choices field

class Person(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField(max_length=60)
    shirt_size = models.CharField(max_length=1, choices=SHIRT_SIZES)

>>> p = Person(name="Fred Flintstone", shirt_size="L")
"""


"""
class Runner(models.Model):
    MedalType = models.TextChoices('MedalType', 'GOLD SILVER BRONZE')
    name = models.CharField(max_length=60)
    medal = models.CharField(blank=True, choices=MedalType.choices, max_length=10)
"""


"""
     # Available Meta options

class DemoModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    grade = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)])
    .....
    .....

    class Meta:
        indexes = [
            models.Index(fields=['last_name', 'first_name']),
            models.Index(fields=['first_name'], name='first_name_idx'),
        ]
        db_table = "DemoModel"
        ordering = ['phone']
        unique_together = ['driver', 'restaurant']
        index_together = ["pub_date", "deadline"]
        constraints = [
            models.CheckConstraint(check=models.Q(age__gte=18), name='age_gte_18'),
        ]
        verbose_name = "pizza"
        verbose_name_plural = "stories"
"""



"""
    Force Update

from django.db.models import F

product = Product.objects.get(name='Venezuelan Beaver Cheese')
product.number_sold = F('number_sold') + 1
product.save()

reporter = Reporters.objects.get(name='Tintin')
reporter.stories_filed = F('stories_filed') + 1
reporter.save()


from django.db.models import Q

Model.objects.filter(
    Q(x=1) & Q(y=2)
)

Model.objects.filter(
    Q(x=1) | Q(y=2)
)
"""


"""
    Django Signal

    https://www.pluralsight.com/guides/introduction-to-django-signals


class Inventory(models.Model):
    ....

class Order(models.Model):
    ....

def validate_order(sender, instance, **kwargs):
    pass

def notify_user(sender, instance, **kwargs):
    pass


pre_save.connect(validate_order, sender=Order):
post_save.connect(notify_user, sender=Order)
"""


"""
    Django aggregate & annotate

from django.db.models import Avg, Min, Max, Count

>>> Book.objects.aggregate(Avg('price'))  # -> {'price__avg': 34.36}
>>> Book.objects.aggregate(Max('price'))  # -> {'price__max': 100000.00}
>>> Book.objects.aggregate(price_diff=Max('price', output_field=FloatField()) - Avg('price'))  # -> {'price_diff': 46.85}
>>> Book.objects.aggregate(Avg('price'), Max('price'), Min('price'))

>>> Store.objects.annotate(min_price=Min('books__price'), max_price=Max('books__price'))
"""
