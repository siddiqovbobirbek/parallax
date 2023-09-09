from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Users)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'address']
    list_display_links = ['name', 'email', 'phone', 'address']



    

