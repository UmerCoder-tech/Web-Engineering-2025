from django import forms
from .models import Bewerbung

class BewerbungForm(forms.ModelForm):
    class Meta:
        model = Bewerbung
        exclude = ['status', 'benutzer']  # ← benutzer wird im View gesetzt

