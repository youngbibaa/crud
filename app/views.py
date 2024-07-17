from django.shortcuts import render
from .forms import CustomerForm
from .models import Customer
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

def home(request):
    customers = Customer.objects.all()
    return render(request, "app/home.html", {"user": request.user, "customer": customers})

@login_required
def project_list(request):
    customers = Customer.objects.all()
    return render(request, "app/customer_list.html", {"customers": customers})

def register(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CustomerForm()
    return render(request, "app/register.html", {"form": form})

@login_required
def customers_list(request):
    customers = Customer.objects.all()
    return render(request, "app/customers_list.html", {"customers": customers})


@login_required
def toggle_customer_status(request, pk):
    customer = get_object_or_404(Customer, pk=pk)
    customer.is_active = not customer.is_active
    customer.save()
    return render(request, 'app/customers_list.html',  kwargs={'pk': pk})