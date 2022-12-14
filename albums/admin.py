from django.contrib import admin

from music_app.albums.models import Album


# Register your models here.
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    pass