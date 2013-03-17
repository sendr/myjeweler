from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from myjeweler.apps.employees.models import Group, Employee
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login, authenticate



@login_required
def employees_group_view(request):

	groups = Group.objects.all()
	return render(request, "employees.html",
					{'groups': groups })

@login_required
def employees_group_list(request, id):
	group = get_object_or_404(Group, id=id)
	employees = Employee.objects.filter(group = group)
	return render(request, "employees_item.html",
		{'employees': employees,
		'group': group})

@login_required
def employee_one(request, id):
	employee = get_object_or_404(Employee, id=id)
	return render(request, "employee_one.html",
				{'employee': employee})

@login_required
def	employees_list(request):
	items = Employee.objects.all()
	return render(request, 'employees_list.html',
				{'items': items})


class EmployeeForm(ModelForm):

	class Meta:
		model = Employee
		
@login_required
def create_view(request, id=None):
	if id is not None:
		employee = get_object_or_404(Employee,id=id)
	else:
		employee = None

	if request.GET:
		form = EmployeeForm(request.GET, instance=employee)
		if form.is_valid():
			employee = form.save()
			return redirect(reverse('employee_one', args=[employee.id]))
	else:
		form = EmployeeForm(instance=employee)

	return render(request,'employee_create.html',{
					'form': form, 'employee': employee})


def login_view(login):
	return redirect(reverse('login') + '?next=%s' % reverse('index'))

def logout_view(request):
	logout(request)
	return redirect(reverse('index'))