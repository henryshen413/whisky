from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'icon', 'lvl', 'parent', 'url')

@admin.register(Distillery)
class DistilleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'region', 'owner', 'lon', 'lat')
    list_filter = ('country', 'region')
    search_fields = ['name']

@admin.register(WhiskyInfo)
class WhiskyInfoAdmin(admin.ModelAdmin):
    list_display = ('name', 'abv', 'brand_series', 'distillery', 'bottler')
    list_filter = ('distillery', 'bottler', 'brand_series')
    search_fields = ['name']

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('name', )

@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name', 'country')

@admin.register(Bar)
class BarAdmin(admin.ModelAdmin):
    list_display = ('name', 'country', 'region', 'lon', 'lat')
