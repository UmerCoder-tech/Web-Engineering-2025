from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django import forms

User = get_user_model()

# 🔐 Registrierungsformular
class StudentRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")


# ✅ Registrierung
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # <-- Automatisches Login
            messages.success(request, "Registrierung erfolgreich! Du bist jetzt eingeloggt.")
            return redirect("dashboard")  # Oder wohin du willst
    else:
        form = StudentRegistrationForm()
    return render(request, "bewerbung/register.html", {"form": form})



# 🔐 Login
def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Login fehlgeschlagen. Bitte überprüfe deine Daten.")
    return render(request, "bewerbung/login.html")


# 🏠 Dashboard
def dashboard(request):
    return render(request, 'bewerbung/dashboard.html')
