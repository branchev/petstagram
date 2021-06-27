from django import forms

from petstagram.common.models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        widgets = {
            'comment': forms.Textarea(
                attrs={
                    'class': 'form-control rounded-2'
                },
            ),
        }
