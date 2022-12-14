from django.contrib.auth import get_user_model
from django.db import models

from music_app.singers.models import Singer


# Create your models here.
UserModel = get_user_model()

class Comment(models.Model):
    comment_text = models.CharField(
        max_length=400,
        null=False,
        blank=False,
    )

    publication_time_and_date = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=True,
    )

    singer = models.ForeignKey(
        Singer,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
    )

    owner = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
        null=True,
        blank=True,
    )