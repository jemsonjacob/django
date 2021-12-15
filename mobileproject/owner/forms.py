from django import forms
from django.forms import ModelForm

from owner.models import Mobile
from owner.models import Order


class MobileForm(ModelForm):
    class Meta:
        model=Mobile
        fields="__all__"


    def clean(self):
        cleaned_data = super().clean()
        mobile_name = cleaned_data["mobile_name"]
        price = cleaned_data["price"]
        stocks = cleaned_data["stocks"]
        mobiles=Mobile.objects.filter(mobile_name=mobile_name)
        if mobiles:
            msg="this name already exists"
            self.add_error("mobile_name",msg)
        if int(price) < 0:
            msg = "invalid price"
            self.add_error("price", msg)
        if int(stocks) < 0:
            msg = "invalid stocks"
            self.add_error("stocks", msg)


class RegistrationForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))

class MobileEditForm(ModelForm):
    class Meta:
        model=Mobile
        fields="__all__"


class MobileSearchForm(forms.Form):
     mobile_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))

class OrderEditForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=["status","expected_delivery"]
        widgets={
           "status":forms.Select(attrs={"class":'form-select'}),
            "expected_delivery":forms.DateInput(attrs={"type":"date"})
       }

