from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout

from django.views.generic import FormView
from django.urls import reverse_lazy

from . import forms

class login_view(FormView):
    template_name = "users/login.html"
    form_class = forms.LoginForm
    success_url = reverse_lazy("home:index")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=username, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

def log_out(request):
    logout(request)
    return redirect(reverse("home:index"))