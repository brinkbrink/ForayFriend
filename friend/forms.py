from django import forms
from .models import Foraged, ForageType, Foray, Resource, Season

class ForagedForm(forms.ModelForm):
    class Meta:
        model=Foraged
        fields='__all__'