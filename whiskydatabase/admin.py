from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Distillery)
class DistilleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'country', 'owner')

admin.site.register(WhiskyInfo)
