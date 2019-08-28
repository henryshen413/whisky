from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'lvl', 'parent', 'url')

@admin.register(Distillery)
class DistilleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'region', 'owner')

@admin.register(WhiskyInfo)
class WhiskyInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'abv', 'bottler')

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Region)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')

@admin.register(Bar)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'region')
