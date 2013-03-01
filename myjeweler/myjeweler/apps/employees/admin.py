from django.contrib import admin
from myjeweler.apps.employees.models import Employee, Group


admin.site.register(Employee)
admin.site.register(Group)