

#Importiert die path-Funktion zum Definieren von URLs
from django.urls import path

#Importiert die Views aus dem aktuellen Verzeichnis
from . import views


#Definiert die URL-Routen dieser App
urlpatterns = [
    #Startseite oder Home-Seite für alle Besucher
    path('', views.home, name='home'),

    #Seite zur Einreichung einer Bewerbung
    path('bewerbung', views.bewerbung, name='bewerbung'),

    #Kontaktformular-Seite
    path('kontakt', views.kontakt, name='kontakt'),

    #Login-Seite für Benutzer
    path('login', views.login_view, name='login'),

    #Registrierungsseite für neue Benutzer
    path('register', views.register, name='register'),

    #Login-Seite speziell für Admins
    path('admin-login/', views.admin_login_view, name='admin_login'),

    #Admin-Dashboard zur Verwaltung von Bewerbungen
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),

    #Logout-URL für alle Benutzer
    path('logout/', views.logout_view, name='logout'),

    #Profilseite des aktuell eingeloggten Benutzers
    path("profil/", views.mein_profil, name="mein_profil"),

    #Diese Zeile überschreibt die erste ''-Route (home)!
    #path('', views.startseite, name='startseite'),

    #Route zum Löschen einer Bewerbung durch einen Admin (mit Primärschlüssel)
    path('admin-dashboard/bewerbung-loeschen/<int:pk>/', views.bewerbung_loeschen, name='admin_bewerbung_loeschen'),
]
