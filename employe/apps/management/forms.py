from django import forms

from apps.management.models import Employee


class EmployeeDetails(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'email', 'dob', 'department','phone_number','address', 'salary']
