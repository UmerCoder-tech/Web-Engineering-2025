

#Importiert das forms-Modul von Django für die Formularerstellung
from django import forms

#Importiert das benutzerdefinierte User-Modell
from frontend.models import StudentUser

#Importiert das vordefinierte Registrierungsformular von Django
from django.contrib.auth.forms import UserCreationForm


#Erstellt ein benutzerdefiniertes Registrierungsformular auf Basis von UserCreationForm
class StudentRegistrationForm(UserCreationForm):
    class Meta:
        #Gibt an, dass das Formular auf dem Modell StudentUser basiert
        model = StudentUser

        #Definiert die Felder, die im Registrierungsformular angezeigt werden sollen
        fields = ['username', 'email', 'password1', 'password2']
        #username ist weiterhin Pflicht, da REQUIRED_FIELDS in StudentUser "username" enthält
