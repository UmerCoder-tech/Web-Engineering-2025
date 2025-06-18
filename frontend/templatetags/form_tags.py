"""""
from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})

"""

# Importiert das Template-Modul von Django, um benutzerdefinierte Template-Tags oder -Filter zu erstellen
from django import template

# Registriert eine neue Template-Library, in der benutzerdefinierte Filter oder Tags gespeichert werden
register = template.Library()

# Definiert einen benutzerdefinierten Filter mit dem Namen 'add_class'
# Dieser Filter kann in Templates verwendet werden, um einem Formularfeld eine CSS-Klasse hinzuzufügen
@register.filter(name='add_class')
def add_class(field, css_class):
    # Gibt das Feld mit der angegebenen CSS-Klasse im HTML zurück
    # field.as_widget() rendert das HTML für das Formularfeld
    # attrs={"class": css_class} fügt eine CSS-Klasse als Attribut hinzu
    return field.as_widget(attrs={"class": css_class})


