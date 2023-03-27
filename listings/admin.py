from django.contrib import admin

# Register your models here.
from listings.models import Band
from .models import Listing

#Rajout des autres champ à notre interface d'administration 
class BandAdmin(admin.ModelAdmin):
    list_display = ("name","year_formed","genre")

admin.site.register(Band,BandAdmin)

#volée listing
class ListingAdmin(admin.ModelAdmin):
    list_display = ("title","type",'descrption',"year","band")
admin.site.register(Listing,ListingAdmin)