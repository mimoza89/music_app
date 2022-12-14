from django import forms

from music_app.common.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment_text',)
        widgets = {
            'comment_text': forms.Textarea(
                    attrs={
                        'cols': 50,
                        'rows': 10,
                        'placeholder': 'Add a new comment...'
                    },
                ),
            }