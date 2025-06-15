from django.contrib.auth.models import AbstractUser
from django.db import models

# 🔐 Benutzer-Modell
ROLE_CHOICES = [
    ('admin', 'Admin'),
    ('user', 'User'),
]

class StudentUser(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')


# 📄 Bewerbungsdaten
class Bewerbung(models.Model):
    STUDIENGANG_WAHL = [
        ('inf', 'Informatik'),
        ('wiwi', 'Wirtschaftswissenschaften'),
        ('med', 'Medizin'),
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

    name = models.CharField(max_length=100)
    email = models.EmailField()
    
    studiengang = models.CharField(
        max_length=20,
        choices=STUDIENGANG_WAHL,
        default='inf'
    )
    abschluss = models.CharField(
        max_length=20,
        choices=ABSCHLUSS_WAHL,
        default='bachelor'
    )
    form = models.CharField(
        max_length=20,
        choices=FORM_WAHL,
        default='online'
    )
    sprachen = models.CharField(max_length=100, default='Deutsch')
    voraussetzungen = models.TextField(default='Keine Angabe')
    datei = models.FileField(upload_to='bewerbungen/', blank=True, null=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_WAHL,
        default='neu'
    )

    erstellt_am = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.studiengang} - {self.status}"
