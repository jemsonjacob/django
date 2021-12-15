from django import forms

from employee.models import Work
from django.forms import ModelForm


class EmployeeForm(ModelForm):
    class Meta:
        model = Work
        fields="__all__"

        widgets={
            "emp_name":forms.TextInput(attrs={"class":"form-control"}),
            "department":forms.TextInput(attrs={"class":"form-control"}),
            "salary":forms.NumberInput(attrs={"class":"form-control"}),
            "experience":forms.NumberInput(attrs={"class":"form-control"})
        }
        labels={'emp_name':'emp name',
                'department':'department',
                'salary':'salary',
                'experience':'experience'

                }
    # emp_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    # department = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    # salary = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}))
    # experience = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}))

    def clean(self):
        cleaned_data = super().clean()
        emp_name = cleaned_data["emp_name"]
        department = cleaned_data["department"]
        salary = cleaned_data["salary"]
        employees=Work.objects.filter(emp_name=emp_name)
        if employees:
            msg="this name already exists"
            self.add_error("employees_name",msg)
        if int(salary) < 0:
            msg = "invalid salary"
            self.add_error("salary", msg)


class EmployeeEditForm(ModelForm):
    class Meta:
        model = Work
        fields = "__all__"

        widgets = {
            "emp_name": forms.TextInput(attrs={"class": "form-control"}),
            "department": forms.TextInput(attrs={"class": "form-control"}),
            "salary": forms.NumberInput(attrs={"class": "form-control"}),
            "experience": forms.NumberInput(attrs={"class": "form-control"})
        }
        labels = {'emp_name': 'emp name',
                  'department': 'department',
                  'salary': 'salary',
                  'experience': 'experience'

                  }
    # emp_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    # department = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))
    # salary = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}))
    # experience = forms.IntegerField(widget=forms.NumberInput(attrs={'class': "form-control"}))

class EmployeeSearchForm(forms.Form):
     emp_name = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control"}))