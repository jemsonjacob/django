from django import forms
from employer.models import MyUser, CompanyProfile, ApplicationModel, JobModel
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.db import models
from django.forms import ModelForm


class UserRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label="Password Conformation",
                                widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = MyUser
        fields = ["email", "phone", "role", "password1", "password2"]

        widgets = {
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.NumberInput(attrs={"class": "form-control"}),
            "role": forms.Select(attrs={"class": "form-select"})
        }


class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))





class ComProfileCreationForm(ModelForm):
    class Meta:
        model = CompanyProfile
        #fields = "__all__"
        fields = ["company_name","logo","description"]

        widgets = {
            "company_name": forms.TextInput(attrs={"class": "form-control"}),


            "description": forms.TextInput(attrs={"class": "form-control"}),

        }
class AddJobForm(ModelForm):
    class Meta:
        model= JobModel

        fields = ["company","job_name","experience","job_details"]

        # widgets = {
        #     "company_name": forms.TextInput(attrs={"class": "form-control"}),
        #
        #
        #     "description": forms.TextInput(attrs={"class": "form-control"}),
        #
        # }
class Application(forms.ModelForm):
    class Meta:
        model=ApplicationModel
        fields = ["job_name","status"]
        widgets = {
            "job_name": forms.TextInput(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": 'form-select'}),
        }