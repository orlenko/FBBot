from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.conf import settings


def home(request):
    auth_profider = 'Unknown'
    if request.user and not request.user.is_anonymous():
        auth_provider = request.user.social_auth.first().provider
    path = request.path
    setting = settings.APPEND_SLASH
    return render_to_response('fbposter/home.html', context_instance=RequestContext(request, locals()))