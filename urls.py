from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', direct_to_template, {'template': 'index.html'}),
    url(r'^blog/$', direct_to_template, {'template': 'blog.html'}),
    #url(r'^team/$', direct_to_template, {'template': 'team.html'}),
    url(r'^speakers/$', direct_to_template, {'template': 'speakers.html'}),
    # url(r'^djangocircus/', include('djangocircus.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
