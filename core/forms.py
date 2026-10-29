from django import forms
from .models import Area, Publico, Curso

class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields= ['nome']