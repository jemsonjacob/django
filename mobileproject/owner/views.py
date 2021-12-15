from django.shortcuts import render, redirect
from customer.decorator import admin_permission_required
from customer.decorator import sign_in_required
from owner.models import Mobile, Order
from owner import forms
from django.db.models import Count


# Create your views here.
def signupview(request):
    form = forms.RegistrationForm()
    context = {}
    context['form'] = form
    if request.method == "POST":
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect("signin")
        else:
            return render(request, "register.html", {"form": form})
    return render(request, "register.html", {"form": form})


def signinview(request):
    form = forms.LoginForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return redirect("addmobile")
        else:
            return render(request, "signin.html", {"form": form})
    return render(request, "signin.html", {"form": form})



@admin_permission_required
def mobile_create(request, *args, **kwargs):
    form = forms.MobileForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = forms.MobileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listmobile')
        else:
            return render(request, "mobile_add.html", {form: form})
    return render(request, 'mobile_add.html', context)


# 8000:owner/mobiles

@admin_permission_required
def mobile_list(request, *args, **kwargs):
    form = forms.MobileSearchForm()
    mobiles = Mobile.objects.all()
    context = {}
    context['mobiles'] = mobiles
    context['form'] = form
    if request.method == "POST":
        form = forms.MobileSearchForm(request.POST)
        if form.is_valid():
            mobile_name = form.cleaned_data["mobile_name"]
            mobiles = Mobile.objects.filter(mobile_name__contains=mobile_name)
            context["mobiles"] = mobiles
            return render(request, "mobile_list.html", context)
    return render(request, "mobile_list.html", context)


# 8000/owner/mobiles/change/{id}

@admin_permission_required
def mobile_update(request, id, *args, **kwargs):
    mobile = Mobile.objects.get(id=id)

    form = forms.MobileEditForm(instance=mobile)
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = forms.MobileEditForm(request.POST, instance=mobile, files=request.FILES)
        if form.is_valid():

            form.save()
            return redirect('listmobile')
    return render(request, "mobile_edit.html", context)


# 8000/owner/remove/{id}

@admin_permission_required
def mobile_remove(request, id, *args, **kwargs):
    mobile = Mobile.objects.get(id=id)
    mobile.delete()
    return redirect('listmobile')


@admin_permission_required
def mobile_detail(request, id, *args, **kwargs):
    mobile = Mobile.objects.get(id=id)
    context = {}
    context['mobile'] = mobile
    return render(request, "mobile_detail.html", context)


@admin_permission_required
def dashboard(request, *args, **kwargs):
    stocks = Mobile.objects.all().order_by("stocks")
    reports = Order.objects.values("product__mobile_name").annotate(counts=Count("product"))

    orders = Order.objects.filter(status="ordered")
    context = {"orders": orders, "reports": reports}

    return render(request, 'dashboard.html', context)


@admin_permission_required
def dashboard_edit(request, id, *args, **kwargs):
    form = forms.OrderEditForm()
    order = Order.objects.get(id=id)
    context = {'form': form}
    if request.method == "POST":
        form = forms.OrderEditForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    return render(request, 'dashboard_edit.html', context)