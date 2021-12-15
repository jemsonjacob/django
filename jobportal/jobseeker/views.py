from django.contrib import messages
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, UpdateView
from django_filters.views import FilterView

from employer.forms import Application
from .filters import JobFilter
from employer.models import JobseekerProfile, ApplicationModel, JobModel
from jobseeker import forms


class JobSeekerHome(TemplateView):
    template_name = "jobseeker/jhome.html"


class AddProfileView(CreateView):
    model = JobseekerProfile
    form_class = forms.ProfileForm
    template_name = "jobseeker/jprofileadd.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect("jhome")
        else:
            return render(request, self.template_name, {"form": form})


class JProfileListView(ListView):
    model = JobseekerProfile
    template_name = "jobseeker/jprofilelist.html"
    context_object_name = "profiles"


class JEditProfile(UpdateView):
    model = JobseekerProfile
    template_name = "jobseeker/jprofileedit.html"
    form_class = forms.ProfileForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("jprofilelist")


class JobView(ListView):
    model = JobModel
    template_name = "jobseeker/jlist.html"
    context_object_name = "jobs"

class JobSearchView(FilterView):
    model = JobseekerProfile
    template_name = "jobseeker/jlist.html"
    context_object_name = "jobs"
    filterset_class = JobFilter

class JobApplyView(CreateView):
    model = ApplicationModel
    form_class = forms.Application
    template_name = 'jobseeker/jlist.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.user)
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.files, request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.user = request.user
            application.save()
            messages.info(self.request, 'Successfully applied for the job!')
            return redirect("japply")
        else:
            messages.info(self.request, 'Successfully applied for the job!')
            return render(request, self.template_name, {'form': form})
