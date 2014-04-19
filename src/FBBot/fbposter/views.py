from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.conf import settings
from .datasources import limerick, pirozhok
from .models import FacebookStatus
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect


def home(request):
    auth_profider = 'Unknown'
    if request.user and not request.user.is_anonymous():
        social_auth = request.user.social_auth.first()
        if social_auth:
            auth_provider = social_auth.provider
    path = request.path
    setting = settings.APPEND_SLASH
    msgs = FacebookStatus.objects.filter(status='approved', publish_timestamp=None)[:10]
    return render_to_response('fbposter/home.html', context_instance=RequestContext(request, locals()))


@login_required
def mock_populate(request):
    if request.method == 'POST':
        for _i in range(10):
            for source in (limerick, pirozhok):
                FacebookStatus.objects.create(author=request.user,
                                              message=source.get_message())
    return HttpResponseRedirect('/')