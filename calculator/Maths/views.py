from django.shortcuts import render
from Maths import forms


def index(request):
    return render(request, 'index.html')


def add_numbers(request):
    form = forms.CalculationForm()
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = forms.CalculationForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            res = num1 + num2
            form['result'] = res
            return render(request, "addition.html", {"form": form})
    return render(request, "addition.html", {"form": form})


def sub_numbers(request):
    form = forms.CalculationForm()
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = forms.CalculationForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            res = num1 - num2
            context['result'] = res
            return render(request, "subtraction.html", context)
    return render(request, "subtraction.html", context)


def mul_numbers(request):
    form = forms.CalculationForm()
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = forms.CalculationForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            res = num1 * num2
            context['result'] = res
            return render(request, "multiplication.html", context)
    return render(request, "multiplication.html", context)


def div_numbers(request):
    form = forms.CalculationForm()
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = forms.CalculationForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']
            num2 = form.cleaned_data['num2']
            res = num1 / num2
            context['result'] = res
            return render(request, "division.html", context)
    return render(request, "division.html", context)


def cube_numbers(request):
    form = forms.CalculationForm()
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = forms.CalculationForm(request.POST)
        if form.is_valid():
            num1 = form.cleaned_data['num1']

            res = num1 * num1 * num1
            context['result'] = res
            return render(request, "cube.html", context)
    return render(request, "cube.html", context)
