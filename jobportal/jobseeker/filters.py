import django_filters
from employer.models import JobModel
from django import forms


class JobFilter(django_filters.FilterSet):
    job_name = django_filters.ModelChoiceFilter(queryset=JobModel.objects.all(),
                                                widget=forms.Select(attrs={'class': 'form-select w-50'}))

    class Meta:
        model = JobModel
        fields = ["job_name"]
