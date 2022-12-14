from django.contrib.auth import get_user_model
from django.db import models
from music_app.singers.models import Singer
# Create your models here.
UserModel = get_user_model()


class Album(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
    )

    released_by = models.ForeignKey(
        Singer,
        blank=True,
        on_delete=models.RESTRICT,
    )


    year_released = models.PositiveIntegerField()

    number_of_songs = models.PositiveIntegerField()

    owner = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )