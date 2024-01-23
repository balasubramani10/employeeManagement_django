from django.contrib import admin
from employee_data.models import *
from payRoll_data.models import *
# Register your models here.


class SalaryAdmin(admin.StackedInline):
    model = Salary
class Attendance_Admin(admin.StackedInline):
    model = Attendance

class EmployeeAdmin(admin.ModelAdmin):
    inlines = [Attendance_Admin, SalaryAdmin]

admin.site.register(Employee, EmployeeAdmin)

admin.site.register(Designation)