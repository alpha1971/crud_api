from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(todo)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'Description', 'Completed','Created_by') 