from django import forms
from .models import Bewerbung

class BewerbungForm(forms.ModelForm):
    class Meta:
        model = Bewerbung
        exclude = ['status', 'erstellt_am']  # <- Wichtig
        widgets = {
            'sprachen': forms.TextInput(attrs={'placeholder': 'z. B. Englisch, Deutsch'}),
            'voraussetzungen': forms.Textarea(attrs={'rows': 4}),
        }
