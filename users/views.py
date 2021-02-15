from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout

from django.views import View

from . import forms

def login_view(request):
    if request.method == "GET":
        form = forms.LoginForm()
        return render(request, "users/login.html", {"form": form})

    elif request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse("home:index"))
        return render(request, "users/login.html", {"form": form})

def log_out(request):
    logout(request)
    return redirect(reverse("home:index"))