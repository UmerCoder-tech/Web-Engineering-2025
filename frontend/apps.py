"""""
from django.apps import AppConfig


class FrontendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'frontend'

"""

# Importiert die AppConfig-Klasse, die verwendet wird, um Konfigurationsinformationen für eine Django-App bereitzustellen
from django.apps import AppConfig


# Definiert eine Konfigurationsklasse für die App 'frontend'
class FrontendConfig(AppConfig):
    # Gibt an, welcher AutoField-Typ standardmäßig für automatisch erzeugte Primärschlüssel verwendet werden soll
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Der Name der App, wie sie im Projekt registriert ist (z. B. in INSTALLED_APPS)
    name = 'frontend'

