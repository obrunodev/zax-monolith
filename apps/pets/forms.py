from django import forms
from shared.forms import BaseModelForm
from apps.pets.models import Pet

class PetForm(BaseModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'species', 'breed', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(
                attrs={'type': 'date', 'column_classes': 'col-md-6'},
                format='%Y-%m-%d'
            ),
        }