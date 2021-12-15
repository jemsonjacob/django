from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from clinicadmin.models import Doctor

from patient import forms


# Create your views here.


def signup(request):
    form = forms.UserRegistrationForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            return render(request, "patient/signup.html", {'form': form})
    return render(request, "patient/signup.html", context)


def signin(request):
    form = forms.LoginForm()
    context = {}
    context['form'] = form

    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('user_home')
            else:
                messages.error(request, "invalid user detected")
                return redirect('signin')
    return render(request, 'patient/signin.html', context)


def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("signin")
    else:
        return redirect("signin")


def user_home(request):
    doctors = Doctor.objects.all()
    context = {}
    context['doctors'] = doctors
    return render(request, 'patient/home.html', context)




def appointment_create(request, a_id):
    doctor = Doctor.objects.get(id=a_id)
    form = forms.AppointmentForm(initial={"patient_name": doctor})

    context = {"form": form, "doctor": doctor}
    if request.method == "POST":
        form = forms.AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()

            messages.success(request, "successfull ")
            return redirect("user_home")
        else:
            return render(request, 'patient/appointment_create.html', {"form": form})

    return render(request, 'patient/appointment_create.html', context)
