from django.db import models

from employe.custom import DateTimeModel


class Employee(DateTimeModel):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=True, max_length=30)
    dob = models.DateField(null=True)
    department = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    address = models.CharField(null=True, blank=True,max_length=40)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)