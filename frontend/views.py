
#Standard-Django-Imports
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages  # Für Feedbacknachrichten an den Nutzer
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.conf import settings

#Modelle und Formulare der App
from .models import StudentUser, Bewerbung
from .forms import BewerbungForm
from .registrieren import StudentRegistrationForm
from mail.email import sende_bestaetigungs_email


#Startseite zeigt alle registrierten Nutzer
def home(request):
    bewerber_liste = StudentUser.objects.all()
    return render(request, 'home.html', {'bewerber': bewerber_liste})


#Bewerbungsseite nur für eingeloggte Nutzer
@login_required
def bewerbung(request):
    if request.method == "POST":
        form = BewerbungForm(request.POST, request.FILES)
        if form.is_valid():
            bewerbung = form.save(commit=False)
            bewerbung.status = "neu"              #Initialstatus setzen
            bewerbung.benutzer = request.user     #Bewerber dem eingeloggten Nutzer zuordnen
            bewerbung.save()
            messages.success(request, "Bewerbung erfolgreich eingereicht!")
            return redirect("mein_profil")
        else:
            messages.error(request, "Fehler beim Absenden der Bewerbung.")
    else:
        form = BewerbungForm()
    return render(request, "bewerbung.html", {"form": form})


#Kontaktseite rein statisch
def kontakt(request):
    return render(request, 'kontakt.html')


#Login-Funktion für reguläre Benutzer
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get("next", "home")
            return redirect(next_url)
        else:
            messages.error(request, "Ungültige Zugangsdaten.")
    return render(request, "login.html")


#Registrierung neuer Benutzer
def register(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registrierung erfolgreich!")
            return redirect("home")
    else:
        form = StudentRegistrationForm()
    return render(request, "register.html", {"form": form})


#Login für Admins – zusätzlich: Prüfung, ob is_staff gesetzt ist
def admin_login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect("admin_dashboard")
        else:
            messages.error(request, "Zugang verweigert oder falsche Daten.")
    return render(request, "admin_login.html")


#Admin-Dashboard zur Bewerbungskontrolle
@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect("login")

    if request.method == "POST":
        bewerbung_id = request.POST.get("bewerbung_id")
        aktion = request.POST.get("aktion")

        try:
            bewerbung = Bewerbung.objects.get(id=bewerbung_id)

            if aktion == "annehmen":
                bewerbung.status = "angenommen"
            elif aktion == "ablehnen":
                bewerbung.status = "abgelehnt"

            bewerbung.save()

            #E-Mail-Bestätigung an Bewerber
            sende_bestaetigungs_email(bewerbung.email, bewerbung.status, bewerbung.name)

        except Bewerbung.DoesNotExist:
            messages.error(request, "Bewerbung nicht gefunden.")

        return redirect("admin_dashboard")

    #Bewerbungen an das Dashboard übergeben
    bewerbungen = Bewerbung.objects.all()
    return render(request, "frontend/admin_dashboard.html", {"bewerbungen": bewerbungen})


#Profilansicht für eingeloggte Benutzer mit ihren eigenen Bewerbungen
@login_required
def mein_profil(request):
    bewerbungen = Bewerbung.objects.filter(benutzer=request.user)
    return render(request, "frontend/mein_profil.html", {
        "bewerbungen": bewerbungen,
    })


#Admin-Funktion zum Löschen einer Bewerbung
@user_passes_test(lambda u: u.is_staff)
def bewerbung_loeschen(request, pk):
    bewerbung = get_object_or_404(Bewerbung, pk=pk)
    bewerbung.delete()
    return redirect('admin_dashboard')


#Alternative Startseite (ggf. doppelt mit 'home')
def startseite(request):
    return render(request, 'startseite.html')


#Logout für alle Nutzer
def logout_view(request):
    logout(request)
    return redirect("home")
