from django import forms

from petstagram.core.forms import BootstrapFormMixin
from petstagram.pets.models import Pet


class PetCreateForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'


class PetEditForm(PetCreateForm):
    class Meta:
        model = Pet
        fields = '__all__'
        widgets = {
            'type': forms.TextInput(
                attrs={
                    'readonly': 'readonly'
                }
            )
        }
