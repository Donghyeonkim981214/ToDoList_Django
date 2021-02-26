from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.views.generic import FormView

from django.views.generic import DetailView
from . import models as user_models

from django.views.generic import UpdateView

from django.contrib.auth.views import PasswordChangeView

from . import forms

from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import LoggedOutOnlyView, CreatorOnlyView

class log_in(LoggedOutOnlyView, LoginView):
    template_name = "users/login.html"

def log_out(request):
    logout(request)
    return redirect(reverse("home:home"))

class sign_up(LoggedOutOnlyView, FormView):

    template_name = "users/signup.html"
    form_class = forms.SignupForm
    success_url = reverse_lazy("home:home")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class user_profile(LoginRequiredMixin, CreatorOnlyView, DetailView):
    login_url = '/users/login/'

    model = user_models.User
    context_object_name = "user_obj"
    template_name = "users/profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class profile_update(LoginRequiredMixin, UpdateView):
    model = user_models.User
    template_name = "users/update_profile.html"
    fields = (
        "first_name",
        "last_name",
        "avatar",
        "gender",
        "bio",
        "birthday",
    )

    def get_object(self, queryset=None):
        return self.request.user

class password_update(LoginRequiredMixin, PasswordChangeView):

    template_name = "users/update_password.html"
    success_url = reverse_lazy('users:login')