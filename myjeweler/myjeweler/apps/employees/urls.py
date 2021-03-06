from django.conf.urls import patterns, url


urlpatterns = patterns('myjeweler.apps.employees.views',
    url(r'^$', 'employees_group_view', name ='employees_group_view'),
    url(r'^employees_group_list/(?P<id>\d+)/$', 'employees_group_list', name = 'employees_group_list'),
    url(r'^(?P<id>\d+)/$', 'employee_one', name = 'employee_one'),
    url(r'^employees_list/$', 'employees_list', name ='employees_list'),
)