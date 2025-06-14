from django import forms
from frontend.models import StudentUser
from django.contrib.auth.forms import UserCreationForm

class StudentRegistrationForm(UserCreationForm):
    class Meta:
        model = StudentUser
        fields = ['username', 'email', 'password1', 'password2']
