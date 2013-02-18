from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'myjeweler.views.index', name='index'),
	url(r'^rings/$', 'myjeweler.views.rings', name='rings'),
	url(r'^earrings/$', 'myjeweler.views.earrings', name='earrings'),
	url(r'^pendants/$', 'myjeweler.views.pendants', name='pendants'),
    url(r'^rings/photo/$', 'myjeweler.views.rings_photo', name='photo1'),
    url(r'^enter/$', 'myjeweler.views.enter', name='enter_to'),
    url(r'^registration/$', 'myjeweler.views.registration', name='registration'),


    # Examples:
    # url(r'^$', 'myjeweler.views.home', name='home'),
    # url(r'^myjeweler/', include('myjeweler.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
