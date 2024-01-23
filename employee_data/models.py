from django.db import models
from base.models import BaseModel
from office_data.models import *

# Create your models here.

class Employee(BaseModel):
    
    first_name = models.CharField(max_length = 128, null = False, blank = False)
    last_name = models.CharField(max_length = 128, null = True, blank = True)
    father_name = models.CharField(max_length = 128, null = False, blank = False)
    contact_number = models.IntegerField(unique = True, null = False, blank = False)
    email_id = models.EmailField(unique = True, null = True, blank = True)
    branch = models.ForeignKey(Branch ,related_name = "branch", on_delete = models.CASCADE,  null =True, blank = True)
    department = models.ForeignKey(Department ,related_name = "emp_department", on_delete = models.CASCADE,  null =True, blank = True)
    reporting_to = models.ForeignKey("self",related_name = "reporting", null=True, blank=True, on_delete=models.SET_NULL)
    role = models.ForeignKey(Designation,related_name = "role", on_delete=models.SET_NULL, null=True, blank=True)
    
    


    def gen_email(self):
        return (f"{self.first_name}.{self.last_name}@ouroffice.com").lower()
    def save(self, *args,**kwargs):
        self.email_id = self.gen_email()
        super(Employee, self).save(*args, **kwargs)
    def __str__(self):
        return self.first_name

class Address(BaseModel):
    employee = models.ForeignKey(Employee, on_delete = models.CASCADE)
    line1 = models.CharField(max_length = 64, null = False, blank = False)
    line2 = models.CharField(max_length = 64, null = True, blank = True)
    land_mark = models.CharField(max_length = 128, null = True, blank = True)
    city = models.CharField(max_length = 64, null = False, blank = False)
    pincode = models.CharField(max_length = 6, null = False, blank = False)
    state = models.CharField(max_length = 128, null = False, blank = False)
    def __str__(self):
        return self.employee.employee.first_name
        
class Attendance(BaseModel):
    employee = models.ForeignKey(Employee,related_name = "attendance", on_delete = models.CASCADE)
    date = models.DateField(null = True)
    present = models.BooleanField(default = False)
    def __str__(self):
        return self.employee.first_name

