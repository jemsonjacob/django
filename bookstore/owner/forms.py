from django import forms

from owner.models import Book, Order
from django.forms import ModelForm
from owner.models import Book



class BookForm(ModelForm):
    class Meta:
        model=Book
        fields="__all__"
    # book_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    #author = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    #price = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}))
    # copies = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}))

    def clean(self):
        cleaned_data = super().clean()
        book_name = cleaned_data["book_name"]
        price = cleaned_data["price"]
        copies = cleaned_data["copies"]
        books=Book.objects.filter(book_name=book_name)
        if books:
            msg="this name already exists"
            self.add_error("book_name",msg)
        if int(price) < 0:
            msg = "invalid price"
            self.add_error("price", msg)
        if int(copies) < 0:
            msg = "invalid copies"
            self.add_error("copies", msg)


class RegistrationForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    user_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': "form-control"}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': "form-control"}))

class BookEditForm(ModelForm):
    class Meta:
        model=Book
        fields="__all__"
    # book_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    # author = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    # price = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}))
    # copies = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}))

class BookSearchForm(forms.Form):
     book_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))

class OrderEditForm(forms.ModelForm):
    class Meta:
        model=Order
        fields=["status","expected_delivery"]
        widgets={
           "status":forms.Select(attrs={"class":'form-select'}),
            "expected_delivery":forms.DateInput(attrs={"type":"date"})
       }


