"""""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

ROLE_CHOICES = [
    ('admin', 'Admin'),
    ('user', 'User'),
]

class StudentUser(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return self.get_full_name() or self.email

class Bewerbung(models.Model):
    STUDIENGANG_WAHL = [
    # Informatik
    ('medieninf', 'Medieninformatik'),
    ('data_sci', 'Data Science'),
    ('ai', 'Künstliche Intelligenz'),
    ('swt', 'Softwaretechnik'),

    # Wirtschaft
    ('bwl', 'Betriebswirtschaft'),
    ('vw', 'Volkswirtschaft'),
    ('ibwl', 'Internationale BWL'),
    ('wi_info', 'Wirtschaftsinformatik'),

    # Medizin
    ('humanmed', 'Humanmedizin'),
    ('zahnmed', 'Zahnmedizin'),
    ('medizintech', 'Medizintechnik'),
    ]

    ABSCHLUSS_WAHL = [
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
    ]
    FORM_WAHL = [
        ('online', 'Online'),
        ('praesenz', 'Präsenz'),
    ]
    STATUS_WAHL = [
        ('neu', 'Neu'),
        ('angenommen', 'Angenommen'),
        ('abgelehnt', 'Abgelehnt'),
    ]

    benutzer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='bewerbungen',
        null=True
    )

    name = models.CharField(max_length=100)
    email = models.EmailField()
  
    strasse = models.CharField(max_length=100, blank=True)
    plz = models.CharField(max_length=10, blank=True)
    ort = models.CharField(max_length=50, blank=True)
    land = models.CharField(max_length=50, default='Deutschland')  # Land kannst du optional als Standard behalten



    studiengang = models.CharField(max_length=20, choices=STUDIENGANG_WAHL, default='inf')
    abschluss = models.CharField(max_length=20, choices=ABSCHLUSS_WAHL, default='bachelor')
    form = models.CharField(max_length=20, choices=FORM_WAHL, default='online')
    sprachen = models.CharField(max_length=100, default='Deutsch')

    datei = models.FileField(upload_to='bewerbungen/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_WAHL, default='neu')
    erstellt_am = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.studiengang} - {self.status}"
"""


#Importiert die AbstractUser-Klasse, um ein benutzerdefiniertes User-Modell zu erstellen
from django.contrib.auth.models import AbstractUser

#Importiert das models-Modul, um Datenbankmodelle zu definieren
from django.db import models

#Importiert die Projekt-Einstellungen (z. B. AUTH_USER_MODEL)
from django.conf import settings


#Definiert die möglichen Rollen für Benutzer
ROLE_CHOICES = [
    ('admin', 'Admin'),
    ('user', 'User'),
]

#Benutzerdefiniertes User-Modell, das auf AbstractUser basiert
class StudentUser(AbstractUser):
    #E-Mail-Adresse muss eindeutig sein und dient als Login-Feld
    email = models.EmailField(unique=True)
    
    #Login erfolgt über die E-Mail-Adresse
    USERNAME_FIELD = "email"
    
    #Pflichtfelder beim Erstellen eines Users via createsuperuser
    REQUIRED_FIELDS = ["username"]
    
    #Rolle des Benutzers (z. B. admin oder user)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    #String-Repräsentation des Users im Admin oder Debugging
    def __str__(self):
        return self.get_full_name() or self.email


#Modell zur Speicherung von Bewerbungen
class Bewerbung(models.Model):
    #Auswahlmöglichkeiten für Studiengänge
    STUDIENGANG_WAHL = [
        #Informatik
        ('medieninf', 'Medieninformatik'),
        ('data_sci', 'Data Science'),
        ('ai', 'Künstliche Intelligenz'),
        ('swt', 'Softwaretechnik'),

        #Wirtschaft
        ('bwl', 'Betriebswirtschaft'),
        ('vw', 'Volkswirtschaft'),
        ('ibwl', 'Internationale BWL'),
        ('wi_info', 'Wirtschaftsinformatik'),

        #Medizin
        ('humanmed', 'Humanmedizin'),
        ('zahnmed', 'Zahnmedizin'),
        ('medizintech', 'Medizintechnik'),
    ]

    #Abschlussarten
    ABSCHLUSS_WAHL = [
        ('bachelor', 'Bachelor'),
        ('master', 'Master'),
    ]

    #Studienform
    FORM_WAHL = [
        ('online', 'Online'),
        ('praesenz', 'Präsenz'),
    ]

    #Bewerbungsstatus
    STATUS_WAHL = [
        ('neu', 'Neu'),
        ('angenommen', 'Angenommen'),
        ('abgelehnt', 'Abgelehnt'),
    ]

    #Verknüpft jede Bewerbung mit einem Benutzer (optional – daher null=True)
    benutzer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,           #Löscht alle Bewerbungen, wenn der Benutzer gelöscht wird
        related_name='bewerbungen',         #Ermöglicht z. B. user.bewerbungen.all()
        null=True
    )

    #Persönliche Angaben
    name = models.CharField(max_length=100)
    email = models.EmailField()

    #Adresse (optional, daher blank=True)
    strasse = models.CharField(max_length=100, blank=True)
    plz = models.CharField(max_length=10, blank=True)
    ort = models.CharField(max_length=50, blank=True)
    land = models.CharField(max_length=50, default='Deutschland')  # Standardland gesetzt

    #Studienbezogene Angaben
    studiengang = models.CharField(max_length=20, choices=STUDIENGANG_WAHL, default='inf')
    abschluss = models.CharField(max_length=20, choices=ABSCHLUSS_WAHL, default='bachelor')
    form = models.CharField(max_length=20, choices=FORM_WAHL, default='online')
    sprachen = models.CharField(max_length=100, default='Deutsch')

    #Datei-Upload (optional)
    datei = models.FileField(upload_to='bewerbungen/', blank=True, null=True)

    #Bewerbungsstatus
    status = models.CharField(max_length=20, choices=STATUS_WAHL, default='neu')

    #Automatischer Zeitstempel bei Erstellung
    erstellt_am = models.DateTimeField(auto_now_add=True)

    #String-Repräsentation der Bewerbung
    def __str__(self):
        return f"{self.name} - {self.studiengang} - {self.status}"
