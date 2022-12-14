from django import forms

from music_app.singers.models import Singer
from music_app.core.form_mixins import DisabledFormMixin


class SingerBaseForm(forms.ModelForm):
    class Meta:
        model = Singer
        # fields = '__all__' (not the case, we want to skip `slug`
        fields = ('full_name', 'age', 'country', 'genre', 'albums_issued')
        # exclude = ('slug',)
        labels = {
            'full_name': 'Singer Name',
            'age': 'Age',
            'country': 'Country',
            'genre': 'Genre',
            'albums_issued': 'Number of issued albums',
        }
        widgets = {
            'full_name': forms.TextInput(
                attrs={
                    'placeholder': 'Full name of the singer'
                }
            ),
            'age': forms.NumberInput(
                attrs={
                    'placeholder': 'Age of the singer',
                }
            ),
            'country': forms.TextInput(
                attrs={
                    'placeholder': 'Country of the singer',
                }
            ),
            'genre': forms.TextInput(
                attrs={
                    'placeholder': 'In which genre does the singer sing?'
                }
            ),
            'albums_issued': forms.NumberInput(
                attrs={
                    'placeholder': 'How many albums does the singer have?'
                }
            )
        }

class SingerCreateForm(SingerBaseForm):
    pass

class SingerEditForm(SingerBaseForm):
    pass

class SingerDeleteForm(DisabledFormMixin, SingerBaseForm):
    disabled_fields = ('full_name', 'age', 'genre', 'country', 'albums_issued')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()


    def save(self, commit=True):
        if commit:
            self.instance.delete()
        return self.instance
