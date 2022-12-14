from django import forms

from music_app.albums.models import Album


class AlbumBaseForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('name', 'year_released', 'number_of_songs')
        labels = {
            'name': 'Album Name',
           # 'released_by': 'Type the name of the singer',
            'year_released': 'Year of release',
            'number_of_songs': 'Number of songs',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Name of the album'
                }
            ),
        #    'released_by': forms.TextInput(
         #       attrs={
          #          'placeholder': 'Name of the singer',
           #     }
            #),


            'year_released': forms.NumberInput(
                attrs={
                    'placeholder': 'Year of release',
               }
            ),

            'number_of_songs': forms.NumberInput(
                attrs={
                    'placeholder': 'How many songs are there in the album?'
                }
            )
        }

class AlbumAddForm(AlbumBaseForm):
    pass

class AlbumEditForm(AlbumBaseForm):
    pass