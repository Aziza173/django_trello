from django.urls import path
from .views import register_view, login_view, logout_view, password_reset_view
from django.shortcuts import render

# Bosh sahifa (dashboard)
def dashboard_view(request):
    return render(request, "project/dashboard.html")

urlpatterns = [
    path("", dashboard_view, name="dashboard"),  # Bosh sahifa qo‘shildi
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("password-reset/", password_reset_view, name="password_reset"),
]
