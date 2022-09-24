from __future__ import unicode_literals
from django.contrib import admin
from django.contrib import messages
from django.contrib.auth.models import Group
from .models import Car, SecureFiles, MyBlog, Product
from .forms import CustomProductAdminForm


# admin.site.register(Car)
# admin.site.register(SecureFiles)
# admin.site.register(MyBlog)


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




##################### All About Admin #######################

admin.site.site_header = "Site Header"
admin.site.site_title = "Site Title"
admin.site.site_url = "http://siteurl.com"
admin.site.index_title = "Index Title"
admin.empty_value_display = '**Empty**'


class CommonAction:
    def export_as_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        print("#"*10, request.user)
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response
    
    def demo_action():
        pass
    
    export_as_csv.short_description = "Export Selected"
    demo_action.short_description = "demo action"



class CustomProduct(admin.ModelAdmin, CommonAction):
    form = CustomProductAdminForm

    # fields = ["price", "title", 'is_active']  # display order of db fields
    fieldsets = (
        ('Product_Info', {'fields': ['price','title']}),
        ('Product Available', {'fields': ['is_active']}),
    )
    exclude = ['description'] # dont display this field
    list_display = ['title', 'price', 'is_active']  # object will represnt with this value
    readonly_fields = ["is_active"]
    list_filter = ['title'] # List filter
    search_fields = ["title__startswith", "title__contains"]  # search bar
    actions = ["export_as_csv", 'demo_action', 'make_active']
    list_per_page = 250 # OR list_per_page = sys.maxsize

    def headshot_image(self, obj):
        from django.utils.safestring import mark_safe
        return mark_safe('<img src="{url}" width="{width}" height={height} />'.format(
            url = obj.headshot.url,
            width=obj.headshot.width,
            height=obj.headshot.height,
            )
    )

    def format_a_data(self, obj):
        from django.utils.html import format_html
        result = Product.objects.first()
        return format_html("<b><i>{}</i></b>", result.title)

    
    def has_add_permission(self, request):  # has add permission
        return True if request.user.username == 'admin' else False

    def make_active(modeladmin, request, queryset):
        queryset.update(is_active = 1) 
        messages.success(request, "Selected Record(s) Marked as Active Successfully !!")
  
    def make_inactive(modeladmin, request, queryset): 
        queryset.update(is_active = 0) 
        messages.success(request, "Selected Record(s) Marked as Inactive Successfully !!")
    
    make_active.short_description = "Make Selected Active"
    
    # admin.site.add_action(make_active, "Make Active") 
    # admin.site.add_action(make_inactive, "Make Inactive")
   
    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)


admin.site.unregister(Group)
admin.site.register(Product, CustomProduct)



"""
    Multiple Admin Site

from django.contrib.admin import AdminSite
class EventAdminSite(AdminSite):
    site_header = "UMSRA Events Admin"
    site_title = "UMSRA Events Admin Portal"
    index_title = "Welcome to UMSRA Researcher Events Portal"

event_admin_site = EventAdminSite(name='event_admin')
event_admin_site.register(Epic)


from events.admin import event_admin_site
urlpatterns = [
    path('admin1/', admin.site.urls),
    path('admin2/', event_admin_site.urls),
]


"""