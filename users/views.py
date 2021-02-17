from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.views.generic import FormView

from . import forms

class log_in(LoginView):
    template_name = "users/login.html"

def log_out(request):
    logout(request)
    return redirect(reverse("home:index"))

class sign_up(FormView):

    template_name = "users/signup.html"
    form_class = forms.SignupForm
    success_url = reverse_lazy("home:index")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)