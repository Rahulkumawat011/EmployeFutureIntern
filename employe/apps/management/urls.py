from django.urls import path

from apps.management import views
from apps.management.views import EmployeeListView, AddEmployee, EmployeeDeleteView, EmployeeUpdateView

urlpatterns = [
    path('index',views.index),
    path('employee_list/', EmployeeListView.as_view(), name='employee_list'),
    path('add_employee/', AddEmployee.as_view(), name='add_employee'),
    path('employee_update/<int:pk>/', EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee_delete/<int:pk>/', EmployeeDeleteView.as_view(), name='employee_delete'),
]