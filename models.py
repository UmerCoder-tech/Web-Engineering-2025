from django.contrib.auth.models import AbstractUser
from django.db import models


class StudentUser(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]  # username ist Pflicht für AbstractUser
