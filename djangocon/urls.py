import settings

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^team/$', TemplateView.as_view(template_name='team.html')),

    url(r'', include('speakers.urls', namespace='speakers', app_name='speakers')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('social_auth.urls')),

)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
