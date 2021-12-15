from django.shortcuts import render, redirect
from employee.models import Work
from employee import forms


# Create your views here.


# employee/employees/add
def employee_create(request):
    form = forms.EmployeeForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = forms.EmployeeForm(request.POST)
        if form.is_valid():
            # emp_name = form.cleaned_data["emp_name"]
            # department = form.cleaned_data["department"]
            # salary = form.cleaned_data["salary"]
            # experience = form.cleaned_data["experience"]
            # employee = Work(emp_name=emp_name, department=department, salary=salary, experience=experience)
            form.save()
            return redirect('addemployee')
        else:
            return render(request, "emp_add.html", {form: form})
    return render(request, 'emp_add.html', context)


# 8000:emplooyee/emplopoyees
def employee_list(request):
    form = forms.EmployeeSearchForm()
    employees = Work.objects.all()
    context = {}
    context['employees'] = employees
    context['form'] = form
    if request.method == "POST":
        form = forms.EmployeeSearchForm(request.POST)
        if form.is_valid():
            emp_name = form.cleaned_data["emp_name"]
            employees = Work.objects.filter(emp_name__contains=emp_name)
            context["employees"] = employees
            return render(request, "emp_list.html", context)
    return render(request, "emp_list.html", context)


def employee_update(request, id):
    employee = Work.objects.get(id=id)
    data = {
        "emp_name": employee.emp_name,
        "department": employee.department,
        "salary": employee.salary,
        "experience": employee.experience
    }
    form = forms.EmployeeEditForm(initial=data)
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = forms.EmployeeEditForm(request.POST)
        if form.is_valid():
            # emp_name = form.cleaned_data["emp_name"]
            # department = form.cleaned_data["department"]
            # salary = form.cleaned_data["salary"]
            # experience = form.cleaned_data["experience"]
            # employee.emp_name = emp_name
            # employee.department = department
            # employee.salary = salary
            # employee.experience = experience
            form.save()
            return redirect('listemployee')
    return render(request, "emp_edit.html", context)


def employee_remove(request, id):
    employee = Work.objects.get(id=id)
    employee.delete()
    return redirect('listemployee')


def employee_detail(request, id):
    employee = Work.objects.get(id=id)
    context = {}
    context['employee'] = employee
    return render(request, "emp_detail.html", context)
