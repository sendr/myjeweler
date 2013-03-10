from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404, redirect
from myjeweler.apps.employees.models import Group, Employee
from django.forms import ModelForm




def employees_group_view(request):

	groups = Group.objects.all()
	return render(request, "employees.html",
					{'groups': groups })

def employees_group_list(request, id):
	group = get_object_or_404(Group, id=id)
	employees = Employee.objects.filter(group = group)
	return render(request, "employees_item.html",
		{'employees': employees,
		'group': group})

def employee_one(request, id):
	employee = get_object_or_404(Employee, id=id)
	return render(request, "employee_one.html",
				{'employee': employee})

def	employees_list(request):
	items = Employee.objects.all()
	return render(request, 'employees_list.html',
				{'items': items})


class EmployeeForm(ModelForm):

	class Meta:
		model = Employee
		

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