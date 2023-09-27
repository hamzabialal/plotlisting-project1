from django.contrib import admin
from .models import Listings, Mycontactform
# Register your models here.
@admin.register(Listings)
class Listing_admin(admin.ModelAdmin):
    list_display = ('area', 'location', 'price', 'image', 'title','listing_type')
@admin.register(Mycontactform)
class Mucontactadmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'desc')