from django.contrib.auth.models import AbstractUser
from django.db import models


"""""
# 🔐 Benutzer-Modell
class StudentUser(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
"""

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
    STUDIENGANG_CHOICES = [
        ('bwl', 'BWL'),
        ('inf', 'Informatik'),
        ('med', 'Medizin'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    studiengang = models.CharField(max_length=10, choices=STUDIENGANG_CHOICES)
    eingereicht_am = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} – {self.studiengang}"
