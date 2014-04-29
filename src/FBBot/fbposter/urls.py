from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^$', 'fbposter.views.home', name='home'),
    url(r'^mock-populate$', 'fbposter.views.mock_populate', name='mock-populate'),
    url(r'^message/update$', 'fbposter.views.message_update'),
    url(r'^message/post$', 'fbposter.views.message_post'),
    url(r'^configure/reddit$', 'fbposter.views.configure_reddit', name='configure-reddit'),
)