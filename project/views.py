from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm
from django.contrib import messages

# Ro‘yxatdan o‘tish
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Muvaffaqiyatli ro‘yxatdan o‘tdingiz!")
            return redirect("dashboard")
    else:
        form = UserCreationForm()
    return render(request, "project/register.html", {"form": form})

# Login
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Tizimga muvaffaqiyatli kirdingiz!")
            return redirect("dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "project/login.html", {"form": form})

# Logout
def logout_view(request):
    logout(request)
    messages.success(request, "Tizimdan chiqdingiz.")
    return redirect("login")

# Parolni unutish va tiklash
def password_reset_view(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                request=request,
                use_https=True,
                email_template_name="project/password_reset_email.html",
            )
            messages.success(request, "Parolni tiklash uchun email jo‘natildi.")
            return redirect("login")
    else:
        form = PasswordResetForm()
    return render(request, "project/password_reset.html", {"form": form})
