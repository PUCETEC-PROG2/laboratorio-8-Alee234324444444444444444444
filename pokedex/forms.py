from django import forms 
from .models import Pokemon

class PokemonForm(forms.ModelsForm):
    class Meta: 
        model = Pokemon
        #fields = ['name', 'type', 'weight', 'height', 'trainer', 'picture']
        fields ='__all__'

        widgets = {
            'name': forms.TextInput(attrs={'form-control'}),
            'type': forms.Select(attrs={'form-control'}),
            'weight': forms.NumberInput(attrs={'form-control'}),
            'height': forms.NumberInput(attrs={'form-control'}),
            'trainer': forms.Select(attrs={'form-control'}),  
            'picture': forms.ClearableFileInput(attrs={'form-control-file'})
        }