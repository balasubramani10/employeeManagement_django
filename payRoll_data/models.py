from django.db import models
from base.models import BaseModel
from employee_data.models import *
# Create your models here.

class DateRange(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.start_date} to {self.end_date}"
class Salary(BaseModel):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    date_range = models.ForeignKey(DateRange, on_delete=models.CASCADE)
    def __str__(self) :
        return f"{self.employee.first_name}/{self.date}"

