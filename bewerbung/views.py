from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django import forms

User = get_user_model()


class StudentRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("email", "password1", "password2")


def register(request):
    if request.method == "POST":
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Registrierung erfolgreich! Du kannst dich jetzt einloggen."
            )
            return redirect("login")
    else:
        form = StudentRegistrationForm()
    return render(request, "bewerbung/register.html", {"form": form})

def dashboard(request):
    return render(request, 'bewerbung/dashboard.html')
