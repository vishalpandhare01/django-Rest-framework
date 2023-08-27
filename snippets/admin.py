from django.contrib import admin

# Register your models here.
from .models import Snippet

class snippetAdmin(admin.ModelAdmin):
    list_display = ('created', 'title', 'code','languge')

admin.site.register(Snippet,snippetAdmin)