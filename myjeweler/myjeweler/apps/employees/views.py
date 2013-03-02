from django.views.generic.simple import direct_to_template
from django.shortcuts import render, get_object_or_404
from myjeweler.apps.employees.models import Group, Employee




def employees_group_view(request):

	groups = Group.objects.all()
	return render(request, "employees.html",
					{'groups': groups })

def employees_list(request, id):
	group = get_object_or_404(Group, id=id)
	employees = Employee.objects.filter(group = group)
	return render(request, "employees_item.html",
		{'employees': employees,
		'group': group})
