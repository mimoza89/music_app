from django.contrib import admin
from music_app.songs.models import Song
# Register your models here.
@admin.register(Song)
class SongAdmin(admin.ModelAdmin):
    pass