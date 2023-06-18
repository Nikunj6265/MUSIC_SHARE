from django.contrib import admin
from .models import MusicFile

@admin.register(MusicFile)
class MusicFileModelAdmin(admin.ModelAdmin):
    list_display = ['user','file', 'access', 'allowed_emails']