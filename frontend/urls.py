from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='home'),
    path('bewerbung', views.bewerbung, name='bewerbung'),
    path('kontakt', views.kontakt, name='kontakt'),
    path('login', views.login_view, name='login'),
    path('register', views.register, name='register'),
    path('admin-login/', views.admin_login_view, name='admin_login'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('logout/', views.logout_view, name='logout'),
    path("profil/", views.mein_profil, name="mein_profil")


]