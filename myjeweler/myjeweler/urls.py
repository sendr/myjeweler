from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

admin.autodiscover()


urlpatterns = patterns('',
	url(r'^$', 'myjeweler.views.index', name='index'),
	url(r'^rings/$', 'myjeweler.views.rings', name='rings'),
	url(r'^earrings/$', 'myjeweler.views.earrings', name='earrings'),
	url(r'^pendants/$', 'myjeweler.views.pendants', name='pendants'),
    url(r'^rings/photo_rings1/$', 'myjeweler.views.photo_rings1', name='photo1'),
    url(r'^earrings/photo_earrings1/$', 'myjeweler.views.photo_earrings1', name='photo_earrings1'),
    url(r'^rings/photo_rings1/photo1/$', 'myjeweler.views.photo1', name='photo1'),
    url(r'^create/$', 'myjeweler.apps.employees.views.create_view', name='create'),
    url(r'^edit/(?P<id>\d+)/$', 'myjeweler.apps.employees.views.create_view', name='edit'),

    url(r'^employees_group_view/', include('myjeweler.apps.employees.urls')),

    url(r'^accounts/login_view/$', 'myjeweler.apps.employees.views.login_view', name="login_view"),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="login"),
    url(r'^accounts/logout/$', 'myjeweler.apps.employees.views.logout_view', name="logout"),

    url(r'^accounts/', include('registration.backends.default.urls')),


    # Examples:
    # url(r'^$', 'myjeweler.views.home', name='home'),
    # url(r'^myjeweler/', include('myjeweler.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', "django.contrib.staticfiles.views.serve",
         {'document_root': settings.STATIC_ROOT}),
        (r'^media/(?P<path>.*)$', "django.contrib.staticfiles.views.serve",
         {'document_root': settings.MEDIA_ROOT}),
    )
