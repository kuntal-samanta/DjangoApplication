from __future__ import unicode_literals
from django.contrib import admin
from django.contrib import messages
from django.contrib.auth.models import Group

from .models import *


# One To One
'''
admin.site.register(UserDetails)
'''

# ForeignKey
'''
admin.site.register(Batch)
admin.site.register(Student)
'''

# Many To Many
'''
admin.site.register(Course)
admin.site.register(Person)
'''

# ForeignKey and ManyToManyField --> Through Key
'''
admin.site.register(Person_More)
admin.site.register(Group_More)
admin.site.register(Membership)
'''


admin.site.site_header = "Site Header"
admin.site.site_title = "Site Title"
admin.site.site_url = "http://siteurl.com"
admin.site.index_title = "Index Title"
admin.empty_value_display = '**Empty**'


class CustomProduct(admin.ModelAdmin):
    # fields = ["price", "title", 'is_active']  # display order of db fields
    fieldsets = (
        ('Product_Info', {'fields': ['price','title']}),
        ('Product Available', {'fields': ['is_active']}),
    )
    
    exclude = ['description'] # dont display this field
    list_display = ['title', 'price']  # object will represnt with this value
    list_filter = ['title'] # List filter
    search_fields = ["title__startswith", "title__contains"]  # search bar
    
    def has_add_permission(self, request):  # remove add product option
        return False

    # List operation creation (in select box)
    def make_active(modeladmin, request, queryset):
        queryset.update(is_active = 1) 
        messages.success(request, "Selected Record(s) Marked as Active Successfully !!") 
  
    def make_inactive(modeladmin, request, queryset): 
        queryset.update(is_active = 0) 
        messages.success(request, "Selected Record(s) Marked as Inactive Successfully !!")
    
    admin.site.add_action(make_active, "Make Active") 
    admin.site.add_action(make_inactive, "Make Inactive") 


admin.site.unregister(Group)
admin.site.register(Product, CustomProduct)

