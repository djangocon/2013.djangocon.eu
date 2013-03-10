from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('speakers.views',
    url(r'^$', 'index', name='index'),
    url(r'^speakers/$', 'speakers', name='speakers'),
    url(r'^talks/$', 'talks', name='talks'),
    url(r'^agenda/$', 'agenda', name='agenda'),
)
