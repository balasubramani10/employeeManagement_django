from django.db import models

from base.models import BaseModel
from employee_data.models import *


# Create your models here.

class Branch(BaseModel):
    code = models.IntegerField()
    location = models.CharField(max_length=64, null=True, blank=True)
    contact_number = models.IntegerField()

    def __str__(self):
        return str(self.location)


class Branch_Address(BaseModel):
    branch = models.ForeignKey(
        Branch, related_name="branch_adress", on_delete=models.CASCADE)
    line1 = models.CharField(max_length=64, null=False, blank=False)
    line2 = models.CharField(max_length=64, null=True, blank=True)
    land_mark = models.CharField(max_length=128, null=True, blank=True)
    city = models.CharField(max_length=64, null=False, blank=False)
    pincode = models.CharField(max_length=6, null=False, blank=False)
    state = models.CharField(max_length=128, null=False, blank=False)
    country = models.CharField(max_length=128, null=False, blank=False)

    def save(self, *args, **kwargs):

        self.branch.location = self.city
        self.branch.save()
        super(Branch_Address, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.branch.code)


class Designation(BaseModel):
    designation = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.designation


class Department(BaseModel):
    name = models.CharField(max_length=255)
    floor = models.IntegerField()

    def __str__(self):
        return self.name

    def get_employee_hierarchy(self, manager=None):
        hierarchy = {'manager': manager, 'employees': []}

        if manager:
            employees = Employee.objects.filter(
                department=self, reporting_manager=manager)
        else:
            employees = Employee.objects.filter(
                department=self, reporting_manager=None)

        for employee in employees:
            hierarchy['employees'].append(
                self.get_employee_hierarchy(employee))

        return hierarchy
