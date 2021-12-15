import django_filters
from .models import TimeSheet,MyUser,Batch
from .models import MyUser
from django import forms

class TimeSheetFilter(django_filters.FilterSet):

    batch=django_filters.ModelChoiceFilter(queryset=Batch.objects.all(),widget=forms.Select(attrs={'class':'form-select w-50'}))



    class Meta:
        model=TimeSheet
        fields=['batch']