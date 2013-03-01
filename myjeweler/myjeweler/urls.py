from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('myjeweler.views',
	url(r'^$', 'index', name='index'),
	url(r'^rings/$', 'rings', name='rings'),
	url(r'^earrings/$', 'earrings', name='earrings'),
	url(r'^pendants/$', 'pendants', name='pendants'),
    url(r'^rings/photo_rings1/$', 'photo_rings1', name='photo1'),
    url(r'^enter/$', 'enter', name='enter_to'),
    url(r'^registration/$', 'registration', name='registration'),
    url(r'^earrings/photo_earrings1/$', 'photo_earrings1', name='photo_earrings1'),
    url(r'^rings/photo_rings1/photo1/$', 'photo1', name='photo1'),
    url(r'^employees/$', 'employees', name='employees'),


    # Examples:
    # url(r'^$', 'myjeweler.views.home', name='home'),
    # url(r'^myjeweler/', include('myjeweler.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
