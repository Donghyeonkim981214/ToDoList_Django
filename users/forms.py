from django import forms
from . import models

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get("username")
        password = cleaned_data.get("password")
        try:
            user = models.User.objects.get(username=username)
            if user.check_password(password):
                return cleaned_data
            else:
                self.add_error("password", forms.ValidationError("Password is wrong"))
        except models.User.DoesNotExist:
            self.add_error("username", forms.ValidationError("User does not exist"))

class SignupForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)
    check_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = models.User
        fields = ("first_name", "last_name", "email", "username", "gender", "birthday")

    def clean_check_password(self):
        password = self.cleaned_data.get("password")
        check_password = self.cleaned_data.get("check_password")
        if password != check_password:
            raise forms.ValidationError("Password confirmation does not match")
        else:
            return password

    def save(self):
        user = super().save(commit=False)
        password = self.cleaned_data.get("password")
        user.set_password(password)
        user.save()