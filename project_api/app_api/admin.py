from django.contrib import admin
from .models import *


class Custom_Book(admin.ModelAdmin):
    list_display = ['book_name', 'book_page', 'book_author', 'book_tag']

    def book_author(self, obj):
        return obj.author.author_name
    
    def book_tag(self, obj):
        return obj.tag

admin.site.register(Book, Custom_Book)
admin.site.register(Author)
admin.site.register(Tag)

admin.site.register(School)
admin.site.register(Standerd)
