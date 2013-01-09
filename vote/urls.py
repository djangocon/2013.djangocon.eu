from django.conf.urls.defaults import patterns, url

urlpatterns = patterns('vote.views',
    url(r'^$', 'index', name='index'),
    url(r'^add_vote/(?P<id>\d+)/(?P<kind>\d+)/$', 'add_vote', name='add_vote'),
    url(r'^cancel_vote/(?P<id>\d+)/$', 'cancel_vote', name='cancel_vote'),
)
