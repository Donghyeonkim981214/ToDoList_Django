from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from . import forms

class login_view(LoginView):
    template_name = "users/login.html"

def log_out(request):
    logout(request)
    return redirect(reverse("home:index"))