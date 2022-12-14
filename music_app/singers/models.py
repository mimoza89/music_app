from django.contrib.auth import get_user_model
from django.db import models
#from django.utils.text import slugify
#from music_app.core.model_mixins import StrFromFieldsMixin
# Create your models here.
UserModel = get_user_model()

class Singer(models.Model):
  #  str_fields = ('id', 'full_name')

    full_name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField()

    country = models.CharField(
        max_length=25,
        null=False,
        blank=False,
    )

    genre = models.CharField(
        max_length=15,
        null=False,
        blank=False,
    )

    albums_issued = models.PositiveIntegerField()


    owner = models.ForeignKey(
        UserModel,
        on_delete=models.RESTRICT,
    )





    def save(self, *args, **kwargs):
        # Create/Update
        super().save(*args, **kwargs)

       # if not self.slug:
        #    self.slug = slugify(f'{self.id}-{self.full_name}')

        # Without the `if` the following scenario might happen:
        # The url is `/pets/4-stamat`
        # Rename `stamat` to `stamata`
        # The new url is `/pets/4-stamata`, but `/pets/4-stamat` does not work

        # Update
        return super().save(*args, **kwargs)