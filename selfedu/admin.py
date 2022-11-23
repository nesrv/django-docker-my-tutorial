from django.contrib import admin

# Register your models here.
from .models import *

class UsersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'time_create', 'door_id', 'is_active')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'login')
    list_editable = ('is_active',)
    list_filter = ('is_active', 'time_create')
    prepopulated_fields = {"slug": ("name",)}

class DoorsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}



admin.site.register(Employees, UsersAdmin)
admin.site.register(Doors, DoorsAdmin)