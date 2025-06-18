

#Importiert das forms-Modul von Django für das Erstellen von Formularen
from django import forms

#Importiert das Bewerbung-Modell, auf dem das Formular basiert
from .models import Bewerbung


#Definiert eine ModelForm-Klasse für Bewerbungen
class BewerbungForm(forms.ModelForm):
    #Definiert Auswahlmöglichkeiten für das Sprachfeld
    SPRACHEN_WAHL = [
        ('Deutsch', 'Deutsch'),
        ('Englisch', 'Englisch'),
    ]

    #Fügt dem Formular ein ChoiceField namens "sprachen" hinzu, mit einem Dropdown-Menü (Select-Widget)
    sprachen = forms.ChoiceField(
        choices=SPRACHEN_WAHL,
        widget=forms.Select(attrs={'class': 'form-select'})  # Bootstrap-Klasse für einheitliches Styling
    )

    class Meta:
        #Gibt an, auf welchem Modell das Formular basiert
        model = Bewerbung

        #Liste der Felder, die im Formular angezeigt werden sollen
        fields = [
            'name', 'email',
            'strasse', 'plz', 'ort', 'land',
            'studiengang', 'abschluss', 'form',
            'sprachen', 'datei'
        ]

        #Weist einzelnen Feldern spezifische Widgets mit CSS-Klassen zu, z. B. für Bootstrap-Integration
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
