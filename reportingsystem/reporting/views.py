from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from reporting.models import MyUser, Course, Batch, TimeSheet
from reporting import forms
from .filters import TimeSheetFilter
from django_filters.views import FilterView
from .decorators import signin_required
from django.utils.decorators import method_decorator

# Create your views here.

class AdminHome(TemplateView):
    template_name = "reporting/admin_home.html"
    # def get(self, request, *args, **kwargs):
    #     return render(request, "reporting/admin_home.html")


class AddUser(CreateView):
    model = MyUser
    form_class = forms.AddUserForm
    template_name = "reporting/user_add.html"
    success_url = reverse_lazy("adminhome")

class Users(ListView):
    model = MyUser
    template_name = "reporting/user_list.html"
    context_object_name = "users"


class EditUser(UpdateView):
    model = MyUser
    template_name = "reporting/user_edit.html"
    form_class = forms.UserCreationForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("users")


class CourseCreateView(CreateView):
    model = Course
    form_class = forms.CourseCreationForm
    template_name = "reporting/course_add.html"
    success_url = reverse_lazy("adminhome")


class Courses(ListView):
    model = Course
    template_name = "reporting/course_list.html"
    context_object_name = "courses"


class EditCourse(UpdateView):
    model = Course
    template_name = "reporting/course_edit.html"
    form_class = forms.CourseCreationForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("courses")


class BatchCreateView(CreateView):
    model = Batch
    form_class = forms.BatchCreationForm
    template_name = "reporting/batch_add.html"
    success_url = reverse_lazy("adminhome")


class Batches(ListView):
    model = Batch
    template_name = "reporting/batch_list.html"
    context_object_name = "batches"


class EditBatch(UpdateView):
    model = Batch
    template_name = "reporting/batch_edit.html"
    form_class = forms.BatchCreationForm
    pk_url_kwarg = "id"
    success_url = reverse_lazy("batches")


class SignInView(TemplateView):
    template_name = "reporting/user_login.html"
    form_class = forms.SigninForm

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
                if request.user.is_admin:
                    return redirect('adminhome')
                else:
                    return redirect("userhome")

            else:
                return redirect('userhome')

@method_decorator(signin_required, name='dispatch')
class UserHome(TemplateView):
    template_name = "reporting/user_home.html"

@method_decorator(signin_required, name='dispatch')
class SignOut(TemplateView):
    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("signin")


class AddTimeSheetView(CreateView):
    model = TimeSheet
    form_class = forms.TimeSheetForm
    template_name = 'reporting/add_timesheet.html'

    def get(self,request,*args,**kwargs):
        form=self.form_class(request.user)
        return render(request,self.template_name,{"form":form})


    def post(self, request, *args, **kwargs):
        form = self.form_class(request.user, request.POST)
        if form.is_valid():
            timesheet = form.save(commit=False)
            timesheet.user = request.user
            timesheet.save()
            return redirect('userhome')
        else:
            return render(request, self.template_name, {'form': form})


class TimeSheetView(FilterView):
    model = TimeSheet
    template_name = "reporting/timesheets_list.html"
    context_object_name = "timesheets"
    filterset_class = TimeSheetFilter

    def get_queryset(self):
        if self.request.user.is_admin:
            queryset = self.model.objects.all()
        else:
            queryset = self.model.objects.filter(user=self.request.user)
        return queryset

@method_decorator(signin_required, name='dispatch')
class EditTimeSheetView(UpdateView):
    model = TimeSheet
    template_name = "reporting/edit_timesheet.html"
    form_class = forms.TimeSheetForm
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('listtimesheet')


class Status(TemplateView):
    model = TimeSheet
    pk_url_kwarg = 'id'

    def get(self, request, *args, **kwargs):
        timesheet = self.model.objects.get(id=kwargs['id'])
        timesheet.verified = True
        timesheet.save()
        return redirect('listtimesheet')

class RemoveTimeSheet(DeleteView):
    model=TimeSheet
    pk_url_kwarg = "id"
    template_name = 'reporting/deletetimesheet.html'
    success_url = reverse_lazy('listtimesheet')