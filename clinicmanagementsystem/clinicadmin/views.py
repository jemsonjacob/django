from django.db.models import Count
from django.shortcuts import render, redirect
from clinicadmin import forms
from clinicadmin.forms import LoginForm, RegisterForm
from clinicadmin.models import Doctor
from clinicadmin.models import Appointment


# Create your views here.
def doctor_create(request, *args, **kwargs):
    form = forms.DoctorAddForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = forms.DoctorAddForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('doctorlist')
        else:
            return render(request, "doctor_add.html", {"form": form})

    return render(request, 'doctor_add.html', context)


def doctor_list(request):
    form = forms.DoctorSearchForm()
    doctors = Doctor.objects.all()
    context = {}
    context['doctors'] = doctors
    context['form'] = form
    if request.method == "POST":
        form = forms.DoctorSearchForm(request.POST)
        if form.is_valid():
            doctor_name = form.cleaned_data["doctor_name"]
            doctors = Doctor.objects.filter(doctor_name__contains=doctor_name) | Doctor.objects.filter(
                department__contains=doctor_name)
            context["doctors"] = doctors
            return render(request, "doctor_list.html", context)
    return render(request, "doctor_list.html", context)


def doctor_update(request, id, *args, **kwargs):
    doctor = Doctor.objects.get(id=id)

    form = forms.DoctorEditForm(instance=doctor)
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = forms.DoctorEditForm(request.POST, instance=doctor, files=request.FILES)
        if form.is_valid:
            form.save()
            return redirect('doctorlist')
    return render(request, "doctor_edit.html", context)


def doctor_remove(request, id, *args, **kwargs):
    doctor = Doctor.objects.get(id=id)
    doctor.delete()
    return redirect('doctorlist')


def doctor_detail(request, id, *args, **kwargs):
    doctor = Doctor.objects.get(id=id)
    context = {}
    context['doctor'] = doctor
    return render(request, "doctor_detail.html", context)

def sign_up(request):
    form=RegisterForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect("signin")

    return render(request,'signup.html',context)

def sign_in(request):
    form=LoginForm()
    context={}
    context["form"]=form
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
            print(form.cleaned_data)
            return redirect("doctoradd")
    return render(request,"signin.html",context)


def dashboard(request, *args, **kwargs):
    appoinments = Doctor.objects.all().order_by("doctor_name")

    appoinments = Appointment.objects.filter(status="Onduty")
    context = {"appoinments": appoinments, "reports": reports}

    return render(request, "dashboard.html", context)



def dashboard_edit(request, id, appoinment=None, *args, **kwargs):
    form = forms.DoctorEditForm()
    appointment = Appointment.objects.get(id=id)
    context = {'form': form}
    if request.method == "POST":
        form = forms.DoctorEditForm(request.POST, instance=appoinment)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    return render(request, 'dashboard_edit.html', context)
