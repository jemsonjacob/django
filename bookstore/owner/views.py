from django.shortcuts import render, redirect
from customer.decorator import admin_permission_required
from customer.decorator import sign_in_required
from owner.models import Book, Order
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
            return redirect("addbook")
        else:
            return render(request, "signin.html", {"form": form})
    return render(request, "signin.html", {"form": form})


# owner/books/add
@admin_permission_required
def book_create(request, *args, **kwargs):
    form = forms.BookForm()
    context = {}
    context["form"] = form

    if request.method == "POST":
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            # book_name = form.cleaned_data["book_name"]
            # author = form.cleaned_data["author"]
            # price = form.cleaned_data["price"]
            # copies = form.cleaned_data["copies"]
            # book = Book(book_name=book_name, author=author, price=price, copies=copies)
            form.save()
            return redirect('listbook')
        else:
            return render(request, "book_add.html", {form: form})
    return render(request, 'book_add.html', context)


# 8000:owner/books

@admin_permission_required
def book_list(request, *args, **kwargs):
    form = forms.BookSearchForm()
    books = Book.objects.all()
    context = {}
    context['books'] = books
    context['form'] = form
    if request.method == "POST":
        form = forms.BookSearchForm(request.POST)
        if form.is_valid():
            book_name = form.cleaned_data["book_name"]
            books = Book.objects.filter(book_name__contains=book_name)
            context["books"] = books
            return render(request, "book_list.html", context)
    return render(request, "book_list.html", context)


# 8000/owner/books/change/{id}

@admin_permission_required
def book_update(request, id, *args, **kwargs):
    book = Book.objects.get(id=id)
    # data = {
    #     "book_name": book.book_name,
    #     "author": book.author,
    #     "price": book.price,
    #     "copies": book.copies
    # }
    form = forms.BookEditForm(instance=book)
    context = {}
    context['form'] = form
    if request.method == 'POST':
        form = forms.BookEditForm(request.POST, instance=book, files=request.FILES)
        if form.is_valid():
            # book_name = form.cleaned_data["book_name"]
            # author = form.cleaned_data["author"]
            # price = form.cleaned_data["price"]
            # copies = form.cleaned_data["copies"]
            # book.book_name = book_name
            # book.author = author
            # book.price = price
            # book.copies = copies
            form.save()
            return redirect('listbook')
    return render(request, "book_edit.html", context)


# 8000/owner/remove/{id}

@admin_permission_required
def book_remove(request, id, *args, **kwargs):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('listbook')


@admin_permission_required
def book_detail(request, id, *args, **kwargs):
    book = Book.objects.get(id=id)
    context = {}
    context['book'] = book
    return render(request, "book_detail.html", context)


@admin_permission_required
def dashboard(request, *args, **kwargs):
    stocks = Book.objects.all().order_by("copies")
    reports = Order.objects.values("product__book_name").annotate(counts=Count("product"))

    orders = Order.objects.filter(status="ordered")
    context = {"orders": orders, "reports": reports}

    return render(request, "dashboard.html", context)


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
