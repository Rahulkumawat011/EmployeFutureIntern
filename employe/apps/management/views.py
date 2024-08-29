from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from apps.management.forms import EmployeeDetails
from apps.management.models import Employee


# Create your views here.

def index(request):
    return HttpResponse("hello world")


class AddEmployee(CreateView):
    model = Employee
    # fields = "__all__"
    # fields = ['first_name','last_name']
    form_class = EmployeeDetails
    template_name = 'EmployeeForm.html'
    # success_url = reverse_lazy('create_user')
    success_url = '/employee_list'

# class ProductList(ListView):
#     model = Product
#     template_name = "product_list.html"

# def product_list(request):
#     products = Product.objects.all()
#     return render(request, "product_list.html", context={"products": products})


class EmployeeListView(ListView):
    model = Employee
    template_name = "employelist.html"
    context_object_name = "employees"


class EmployeeUpdateView(UpdateView):
    model = Employee
    fields = ['first_name', 'last_name', 'email', 'dob', 'department', 'phone_number', 'address', 'salary']
    template_name = 'employee_update.html'
    success_url = reverse_lazy('employee_list')

# Delete View


class EmployeeDeleteView(DeleteView):
    model = Employee
    template_name = 'employee_delete.html'
    success_url = reverse_lazy('employee_list')