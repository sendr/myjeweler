from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
	url(r'^$', 'myjeweler.views.index', name='index'),
	url(r'^rings/$', 'myjeweler.views.rings', name='rings'),
	url(r'^earrings/$', 'myjeweler.views.earrings', name='earrings'),
	url(r'^pendants/$', 'myjeweler.views.pendants', name='pendants'),
    url(r'^rings/photo_rings1/$', 'myjeweler.views.photo_rings1', name='photo1'),
    url(r'^enter/$', 'myjeweler.views.enter', name='enter_to'),
    url(r'^registration/$', 'myjeweler.views.registration', name='registration'),
    url(r'^earrings/photo_earrings1/$', 'myjeweler.views.photo_earrings1', name='photo_earrings1'),
    url(r'^rings/photo_rings1/photo1/$', 'myjeweler.views.photo1', name='photo1'),

    url(r'^employees_group_view/', include('myjeweler.apps.employees.urls')),


    # Examples:
    # url(r'^$', 'myjeweler.views.home', name='home'),
    # url(r'^myjeweler/', include('myjeweler.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
