from django.conf.urls import patterns, url


urlpatterns = patterns('myjeweler.apps.employees.views',
    url(r'^$', 'employees_group_view', name ='employees_group_view'),
    url(r'^employees_group_view/employees_list/(?P<id>\d+)/$', 'employees_list', name = 'employees_list'),
)