from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'fbposter.views.home', name='home'),
    url(r'^mock-populate$', 'fbposter.views.mock_populate', name='mock-populate'),
)