from django.contrib import admin
from .models import Baser

@admin.register(Baser)
class BaserAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'link', 'description']
