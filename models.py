from django.db import models

from music_app.albums.models import Album
from music_app.singers.models import Singer


# Create your models here.

class Song(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )

    in_the_album = models.ForeignKey(
        Album,
        blank=True,
        null=True,
        on_delete=models.RESTRICT,
    )

    duration = models.IntegerField(
        null=False,
        blank=False,
    )

    released_by = models.ForeignKey(
        Singer,
        blank=True,
        null=True,
        on_delete=models.RESTRICT,
    )