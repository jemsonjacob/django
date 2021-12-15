from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.shortcuts import redirect

from clinicadmin.models import Doctor


class DoctorAddForm(ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"
        widgets = {'doctor_name': forms.TextInput(attrs={"class": "form-control"}),
                   'department': forms.TextInput(attrs={"class": 'form-control'}),
                   'doctor_time': forms.TimeInput(attrs={"class": 'form-control'}),
                   'doctor_fee': forms.NumberInput(attrs={"class": 'form-control'})
                   }
        labels = {'doctor_name': "DoctorName", 'department': 'Department', 'doctor_time': 'DoctorTime',
                  'doctor_fee': 'DoctorFee'}


class DoctorSearchForm(forms.Form):
    doctor_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))


class DoctorEditForm(ModelForm):
    class Meta:
        model = Doctor
        fields = "__all__"





class RegisterForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))
