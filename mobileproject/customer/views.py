from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from customer import forms
from django.contrib import messages
from owner.models import Mobile, Order
from customer.filters import MobileFilter
from customer.decorator import sign_in_required


# Create your views here.

def signup(request):
    form = forms.UserRegistrationForm()
    context = {}
    context["forms"] = form
    if request.method == "POST":
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("signin")
        else:
            return render(request, "signup.html", {'form': form})
    return render(request, "signup.html", context)


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
                return redirect('user_home')
    return render(request, 'login.html', context)


def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("signin")
    else:
        return redirect("signin")


@sign_in_required
def user_home(request, *args, **kwargs):
    mobiles = Mobile.objects.all()
    context = {}
    context['mobiles'] = mobiles
    return render(request, 'customer/home.html', context)


@sign_in_required
def order_create(request, p_id, *args, **kwargs):
    mobile = Mobile.objects.get(id=p_id)
    form = forms.OrderForm(initial={"product": mobile})

    context = {"form": form, "mobile": mobile}
    if request.method == "POST":
        form = forms.OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            mobile.stocks -= 1
            mobile.save()
            messages.success(request, "order placed")
            return redirect("user_home")
        else:
            return render(request, 'customer/order_create.html', {"form": form})

    return render(request, "customer/order_create.html", context)


@sign_in_required
def order_list(request, *args, **kwargs):
    orders = Order.objects.filter(user=request.user).exclude(status="cancelled")
    context = {"orders": orders}
    return render(request, "customer/order_list.html", context)


@sign_in_required
def cancel_order(request,p_id, *args, **kwargs):
    order = Order.objects.get(id=p_id)
    order.status = "cancelled"
    order.save()
    return redirect("user_home")

@sign_in_required
def mobile_find(request,*args,**kwargs):
    filters = MobileFilter(request.GET, queryset=Mobile.objects.all())
    return render(request, "customer/mobilefilter.html", {"filter": filters})

