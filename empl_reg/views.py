from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login

from .forms import EmployeeForm
from .models import Employee, Position


from django.contrib.auth import authenticate, login

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('employee_insert')
    else:
        return redirect('employee_insert')

def employee_pos(request):
    context = {'employee_pos':Position.objects.all()}
    return render(request, "empl_reg/employee_pos.html", context)


def employee_list(request):
    context = {'employee_list':Employee.objects.all()}
    return render(request, "empl_reg/employee_list.html", context)


def employee_form(request, id = 0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk = id)    #primary key
            form = EmployeeForm(instance = employee)
        return render(request, "empl_reg/employee_form.html", {'form': form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            employee = Employee.objects.get(pk = id)
            form = EmployeeForm(request.POST, instance = employee)

        if form.is_valid():
            form.save()
        return redirect('/employee/list')
    

def employee_delete(request, id):
    employee = Employee.objects.get(pk = id)
    employee.delete()
    return redirect('/employee/list')

def loginPage(request):
    context = {}
    return render(request, 'accounts/login,html', context)