from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings

from .models import StudentUser, Bewerbung
from .forms import BewerbungForm
from .registrieren import StudentRegistrationForm


def home(request):
    bewerber_liste = StudentUser.objects.all()
    return render(request, 'home.html', {'bewerber': bewerber_liste})


# 🔐 Bewerbung nur für eingeloggte Nutzer möglich
@login_required(login_url="login")
def bewerbung(request):
    if request.method == "POST":
        form = BewerbungForm(request.POST, request.FILES)
        if form.is_valid():
            bewerbung = form.save(commit=False)
            bewerbung.status = "neu"
            bewerbung.save()
            messages.success(request, "Bewerbung erfolgreich eingereicht!")
            return redirect("home")
        else:
            messages.error(request, "Fehler beim Absenden des Formulars.")
    else:
        form = BewerbungForm()
    return render(request, "bewerbung.html", {"form": form})


def kontakt(request):
    return render(request, 'kontakt.html')


# 🟡 Login-Logik aktiv
def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get("next", "home")  # nach Login zurück zur vorherigen Seite
            return redirect(next_url)
        else:
            messages.error(request, "Ungültige Zugangsdaten.")
    return render(request, "login.html")


# 🟢 Registrierung
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


# 🔐 Admin Login separat
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


# 🛠 Adminbereich: Bewerbungen ansehen, annehmen, ablehnen + E-Mail
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
                bewerbung.save()

                send_mail(
                    subject="Ihre Bewerbung wurde angenommen",
                    message=(
                        f"Hallo {bewerbung.name},\n\n"
                        f"herzlichen Glückwunsch! Ihre Bewerbung für den Studiengang "
                        f"{bewerbung.get_studiengang_display()} wurde angenommen."
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[bewerbung.email],
                    fail_silently=False,
                )

            elif aktion == "ablehnen":
                bewerbung.status = "abgelehnt"
                bewerbung.save()

                send_mail(
                    subject="Ihre Bewerbung wurde abgelehnt",
                    message=(
                        f"Hallo {bewerbung.name},\n\n"
                        f"leider müssen wir Ihnen mitteilen, dass Ihre Bewerbung für den Studiengang "
                        f"{bewerbung.get_studiengang_display()} abgelehnt wurde."
                    ),
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[bewerbung.email],
                    fail_silently=False,
                )

        except Bewerbung.DoesNotExist:
            messages.error(request, "Bewerbung nicht gefunden.")

        return redirect("admin_dashboard")

    bewerbungen = Bewerbung.objects.all()
    return render(request, "frontend/admin_dashboard.html", {"bewerbungen": bewerbungen})


# 🚪 Logout
def logout_view(request):
    logout(request)
    return redirect("home")
