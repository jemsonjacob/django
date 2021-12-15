from django.forms import ModelForm
from django.views.generic import TemplateView
from datetime import datetime
from reporting.admin import UserCreationForm
from reporting.models import MyUser, Batch, Course, TimeSheet
from django import forms


class AddUserForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ["email", "role", "password1", "password2"]

        def clean(self):
            pass


class BatchCreationForm(ModelForm):
    class Meta:
        model = Batch
        fields = ["course", "batch_name"]
        widgets = {
            "course": forms.TextInput(attrs={"class": "form-control"}),

            "batch_name": forms.TextInput(attrs={"class": "form-control"}),

        }


class CourseCreationForm(ModelForm):
    class Meta:
        model = Course
        fields = ["course_name"]
        widgets = {
            "course_name": forms.TextInput(attrs={"class": "form-control"})
        }


class SigninForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-select '}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-select '}))


class TimeSheetForm(forms.ModelForm):

    def __init__(self,user,*args,**kwargs):
        self.user=user
        super().__init__(*args,*kwargs)

    class Meta:
        model = TimeSheet
        fields = ['batch', 'topic', 'topic_status']
        widgets = {
            'batch': forms.Select(attrs={'class': 'form-select '}),
            'topic': forms.TextInput(attrs={'class': 'form-control'}),
            'topic_status': forms.Select(attrs={'class': 'form-select'}),


        }

    def clean(self):
        cleaned_data = super().clean()
        batch = cleaned_data['batch']

        print(self.user)

        record = TimeSheet.objects.filter(date=datetime.today(), batch=batch,user=self.user)
        if record:
            msg = "already added"
            print(msg)
            self.add_error("topic", msg)
