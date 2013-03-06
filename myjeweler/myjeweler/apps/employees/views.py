
from django.shortcuts import render, get_object_or_404
from myjeweler.apps.employees.models import Group, Employee




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
	