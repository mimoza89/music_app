from enum import Enum

from django.core import validators
from django.db import models
from django.contrib.auth import models as auth_models

from music_app.core.model_mixins import ChoicesEnumMixin
from music_app.core.validators import validate_only_letters


class Gender(ChoicesEnumMixin, Enum):
    male = 'Male'
    female = 'Female'


class AppUser(auth_models.AbstractUser):
    first_name = models.CharField(
        max_length=20,
        validators=(
            validators.MinLengthValidator(2),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=50,
        validators=(
            validators.MinLengthValidator(5),
            validate_only_letters,
        )
    )

    email = models.EmailField(
        unique=True,
    )

    age = models.PositiveIntegerField(
        null=True,
        blank=True
    )

    country = models.CharField(
        max_length=20,
    )

    gender = models.CharField(
        choices=Gender.choices(),
        max_length=Gender.max_len()
    )

    REQUIRED_FIELDS = ['email']
