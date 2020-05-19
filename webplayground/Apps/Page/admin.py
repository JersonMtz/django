from django.contrib import admin
from Apps.Page.models import *

# Register your models here.

class AdminPage(admin.ModelAdmin):
    list_display = ['title','created', 'order',]
    readonly_fields = ("created","updated")

admin.site.register(Pages, AdminPage)