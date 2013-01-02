from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
import settings



urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html')),
    url(r'^blog/$', TemplateView.as_view(template_name='blog.html')),
    url(r'^team/$', TemplateView.as_view(template_name='team.html')),
    url(r'^codeofconduct/$', TemplateView.as_view(template_name='codeofconduct.html')),
    url(r'^speakers/$', TemplateView.as_view(template_name='speakers.html')),

)

if not settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )
