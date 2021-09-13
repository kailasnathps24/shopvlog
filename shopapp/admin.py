from django.contrib import admin
from . models import  *

class categdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name','slug']
admin.site.register(categ,categdmin)

class prodadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['name', 'slug','price','stock','img','available']
    list_editable = ['price','stock','img','available']
admin.site.register(product,prodadmin)



# Register your models here.
