from django.forms import forms, ModelForm

from employer.models import JobseekerProfile, ApplicationModel
from django import forms


class ProfileForm(forms.ModelForm):
    class Meta:
        model = JobseekerProfile
        fields = ["name", "profile_pic", "skill", "resume"]
        widgets = {

            "Skill": forms.TextInput(attrs={"class": "form-control"}),
            "Name": forms.TextInput(attrs={"class": "form-control"}),
        }


# class JobSearchForm(forms.ModelForm):
#     job_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
class Application(forms.ModelForm):
    class Meta:
        model = ApplicationModel
        fields = ["job_name", "status"]
        widgets = {
            "job_name": forms.TextInput(attrs={"class": "form-control"}),
            "status": forms.Select(attrs={"class": 'form-select'}),
        }
