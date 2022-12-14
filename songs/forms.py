from django import forms

from music_app.core.form_mixins import DisabledFormMixin
from music_app.songs.models import Song


class SongBaseForm(forms.ModelForm):
    class Meta:
        model = Song
        # fields = '__all__' (not the case, we want to skip `slug`
        fields = ('name', 'duration', )
        # exclude = ('slug',)
        labels = {
            'name': 'Song Name',
            'duration': 'Duration',
        }
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Name of the song'
                }
            ),
            'duration': forms.NumberInput(
                attrs={
                    'placeholder': 'Duration of the song',
                }
            ),
        }

class SongCreateForm(SongBaseForm):
    pass

class SongEditForm(SongBaseForm):
    pass

class SongDeleteForm(DisabledFormMixin, SongBaseForm):
    disabled_fields = ('name', 'duration')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()


    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
