from django import forms
from naval_app.models import Buque

class BuqueForm(forms.ModelForm):
    class Meta:
        model = Buque
        fields = ["nombre", "imo", "eslora", "manga", "puntal", "tripulantes"]
        widgets = {
            "nombre": forms.TextInput(attrs={'class': 'form-control'}),
            "imo": forms.NumberInput(attrs={'class': 'form-control'}),
            "eslora": forms.NumberInput(attrs={'class': 'form-control'}),
            "manga": forms.NumberInput(attrs={'class': 'form-control'}),
            "puntal": forms.NumberInput(attrs={'class': 'form-control'}),
            "tripulantes": forms.NumberInput(attrs={'class': 'form-control'}),
        }