from django import forms
from .models import Mission, Domaine

class MissionForm(forms.ModelForm):
    class Meta:
        model = Mission
        fields = ["title", "description", "image"]

class DomaineForm(forms.ModelForm):
    class Meta:
        model = Domaine
        fields = ["title", "detail", "desc", "image"]