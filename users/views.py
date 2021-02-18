from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.views.generic import FormView

from django.views.generic import DetailView
from . import models as user_models

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

class user_profile(DetailView):

    model = user_models.User
    context_object_name = "user_obj"
    template_name = "users/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.kwargs)
        return context