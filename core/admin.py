from csv import list_dialects
from django.contrib import admin
from core.models import Item

@admin.register(Item)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'price')
    list_dialects = ('name', 'price')
    search_fields = ('name', 'color', 'price')


# Register your models here.
