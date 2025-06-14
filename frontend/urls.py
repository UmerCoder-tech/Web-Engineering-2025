from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('bewerbung', views.bewerbung, name='bewerbung'),
    path('kontakt', views.kontakt, name='kontakt'),
    path('login', views.login_view, name='login'),
    path('register', views.register, name='register')
]