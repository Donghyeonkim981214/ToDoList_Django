from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout

from django.views import View

from . import forms

class login_view(View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
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