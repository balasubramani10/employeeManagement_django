from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from employee_data.models import *
from datetime import datetime
from office_data.models import *
# Create your views here.


# employee_management/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee, EmployeeSalary, DateRange, Department
from .forms import EmployeeSalaryForm
from django.db.models import Sum
from django.db.models import Q


def add_salary(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)

    if request.method == 'POST':
        form = EmployeeSalaryForm(request.POST)
        if form.is_valid():
            salary_entry = form.save(commit=False)
            salary_entry.employee = employee
            salary_entry.save()
            return redirect('employee_detail', employee_id=employee.id)
    else:
        form = EmployeeSalaryForm()

    return render(request, 'add_salary.html', {'form': form, 'employee': employee})


def update_salary(request, salary_id):
    salary_entry = get_object_or_404(EmployeeSalary, pk=salary_id)

    if request.method == 'POST':
        form = EmployeeSalaryForm(request.POST, instance=salary_entry)
        if form.is_valid():
            form.save()
            return redirect('employee_detail', employee_id=salary_entry.employee.id)
    else:
        form = EmployeeSalaryForm(instance=salary_entry)

    return render(request, 'update_salary.html', {'form': form, 'salary_entry': salary_entry})


def delete_salary(request, salary_id):
    salary_entry = get_object_or_404(EmployeeSalary, pk=salary_id)

    if request.method == 'POST':
        employee_id = salary_entry.employee.id
        salary_entry.delete()
        return redirect('employee_detail', employee_id=employee_id)

    return render(request, 'delete_salary.html', {'salary_entry': salary_entry})


def salary_report(request):
    if request.method == 'POST':
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        department_costs = Department.objects.annotate(
            total_cost=Sum('employee__employeesalary__salary', filter=Q(
                employee__employeesalary__date_range__start_date__lte=end_date, employee__employeesalary__date_range__end_date__gte=start_date))
        ).values('name', 'total_cost')

        return render(request, 'salary_report.html', {'department_costs': department_costs, 'start_date': start_date, 'end_date': end_date})

    return render(request, 'salary_report.html')


def index(req):
    allemp = Employee.objects.all()
    context = {'allemp': allemp}
    return render(req, 'index.html', context)


def employee_detail(request, employee_id):
    employee = get_object_or_404(Employee, pk=employee_id)
    return render(request, 'employee_detail.html', {'employee': employee})


def view_employee(request):
    if request.GET.get("search"):
        user_input = request.GET.get("search")
        employees = Employee.objects.filter(first_name__icontains=user_input)

        cur_date = datetime.now()
        context = {"employees": employees,  "cur_date": cur_date}
    else:
        employees = Employee.objects.all()
        cur_date = datetime.now()
        context = {"employees": employees, "cur_date": cur_date}

    return render(request, "db_admin/index.html", context)


def del_emp(request, u_id):
    emp = Employee.objects.get(u_id=u_id)
    emp.delete()
    return redirect("/")
