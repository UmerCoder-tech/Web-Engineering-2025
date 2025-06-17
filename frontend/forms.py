from django import forms
from .models import Bewerbung
"""""
class BewerbungForm(forms.ModelForm):
    class Meta:
        model = Bewerbung
        exclude = ['status', 'benutzer']  # ← benutzer wird im View gesetzt

"""

from django import forms
from .models import Bewerbung

class BewerbungForm(forms.ModelForm):
    SPRACHEN_WAHL = [
        ('Deutsch', 'Deutsch'),
        ('Englisch', 'Englisch'),
    ]

    sprachen = forms.ChoiceField(
        choices=SPRACHEN_WAHL,
        widget=forms.Select(attrs={'class': 'form-select'})
    )

    class Meta:
        model = Bewerbung
        fields = [
            'name', 'email',
            'strasse', 'plz', 'ort', 'land',
            'studiengang', 'abschluss', 'form',
            'sprachen', 'datei'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'strasse': forms.TextInput(attrs={'class': 'form-control'}),
            'plz': forms.TextInput(attrs={'class': 'form-control'}),
            'ort': forms.TextInput(attrs={'class': 'form-control'}),
            'land': forms.TextInput(attrs={'class': 'form-control'}),
            'studiengang': forms.Select(attrs={'class': 'form-select'}),
            'abschluss': forms.Select(attrs={'class': 'form-select'}),
            'form': forms.Select(attrs={'class': 'form-select'}),
            'datei': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
