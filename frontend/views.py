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



# Create your views here.
