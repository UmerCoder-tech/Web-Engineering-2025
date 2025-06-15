from django.shortcuts import render
from frontend.models import StudentUser

def home(request):
    return render(request, 'home.html')

# frontend/views.py
def home(request):
    bewerber_liste = StudentUser.objects.all()
    return render(request, 'home.html', {'bewerber': bewerber_liste})


def bewerbung(request):
    return render(request, 'bewerbung.html')

def kontakt(request):
    return render(request, 'kontakt.html')

def login_view(request):
    return render(request, 'login.html')

from .registrieren import StudentRegistrationForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import redirect

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


from django.contrib.auth import authenticate, login

from django.contrib.auth import authenticate, login
from django.contrib import messages

def admin_login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, email=email, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect("admin_dashboard")  # Zielseite für Admin
        else:
            messages.error(request, "Zugang verweigert oder falsche Daten.")
    return render(request, "admin_login.html")


# views.py
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Bewerbung

@login_required
def admin_dashboard(request):
    if not request.user.is_staff:
        return redirect("login")  # normale User blockieren

    bewerbungen = Bewerbung.objects.all()
    return render(request, "frontend/admin_dashboard.html", {"bewerbungen": bewerbungen})

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect("home")

# Create your views here.
