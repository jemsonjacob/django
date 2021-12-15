from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from clinicadmin.models import Appointment
from django.forms import ModelForm


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ["first_name", "username", "email"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"})
        }


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ['patient_name', 'gender','address','phone', 'date']
