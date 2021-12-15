from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView

from employer.decorators import signin_required
from employer.forms import ComProfileCreationForm
from employer.models import MyUser, CompanyProfile, JobModel, ApplicationModel
from employer import forms


# Create your views here.


class AdminHome(TemplateView):
    template_name = "employer/company_home.html"


class AddUser(CreateView):
    model = MyUser
    form_class = forms.UserRegistrationForm
    template_name = "employer/user_add.html"
    success_url = reverse_lazy("login")


# @method_decorator(signin_required, name='dispatch')
class SignInView(TemplateView):
    template_name = "employer/user_login.html"
    form_class = forms.LoginForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)
            if user:
                login(request, user)
                if request.user.role == "jobseeker":
                    return redirect('jhome')
                else:
                    return redirect("companyhome")

            else:
                return redirect('jhome')


class SignOut(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("login")


class CProfileHome(TemplateView):
    template_name = "employer/profile_home.html"


class ComProfileCreateView(CreateView):
    model = CompanyProfile
    form_class = forms.ComProfileCreationForm
    template_name = "employer/profile_add.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            company = form.save(commit=False)
            company.company = request.user
            company.save()
            return redirect("cprofilehome")
        else:
            return render(request, self.template_name, {"form": form})


class ComProfileListView(ListView):
    model = CompanyProfile
    template_name = "employer/profile_list.html"
    context_object_name = "companies"


# <h1>Name: {{request.user.name}}</h1>

class EditComProfile(UpdateView):
    model = CompanyProfile
    template_name = "employer/profile_edit.html"
    form_class = forms.ComProfileCreationForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("listcomprofile")


class DeleteCprofile(DeleteView):
    model = CompanyProfile
    pk_url_kwarg = "id"
    template_name = 'employer/deletecprofile.html'
    success_url = reverse_lazy('listcomprofile')


class JobHome(TemplateView):
    template_name = "employer/job_home.html"


class AddJob(CreateView):
    model = JobModel
    form_class = forms.AddJobForm
    template_name = "employer/job_add.html"
    success_url = reverse_lazy("companyhome")


class JobListView(ListView):
    model = JobModel
    template_name = "employer/job_list.html"
    context_object_name = "jobs"




class EditJobView(UpdateView):
    model = JobModel
    template_name = "employer/job_edit.html"
    form_class = forms.AddJobForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("listjob")






class ApplicationView(ListView):
    model = ApplicationModel
    template_name = 'employer/applications.html'
    context_object_name = 'applicants'

    def get_queryset(self):

        return self.model.objects.filter(user_id=self.request.user.id)

