from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'lvl', 'parent', 'url')

@admin.register(Distillery)
class DistilleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'country', 'owner')

admin.site.register(WhiskyInfo)
