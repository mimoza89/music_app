from django.contrib import admin

from music_app.singers.models import Singer


# Register your models here.
@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    pass