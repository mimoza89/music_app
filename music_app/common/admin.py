from django.contrib import admin

from music_app.common.models import Comment



@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass