from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.conf import settings
from .datasources import limerick, pirozhok
from .models import FacebookStatus
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.http.response import HttpResponse
import facebook
import datetime


def home(request):
    auth_profider = 'Unknown'
    msgs = []
    if request.user and not request.user.is_anonymous():
        msgs = FacebookStatus.objects.filter(status='approved', publish_timestamp=None, author=request.user)[:10]
        social_auth = request.user.social_auth.first()
        if social_auth:
            auth_provider = social_auth.provider
    path = request.path
    setting = settings.APPEND_SLASH
    return render_to_response('fbposter/home.html', context_instance=RequestContext(request, locals()))


@login_required
def mock_populate(request):
    if request.method == 'POST':
        for _i in range(10):
            for source in (limerick, pirozhok):
                FacebookStatus.objects.create(author=request.user,
                                              message=source.get_message())
    return HttpResponseRedirect('/')

def message_update(request):
    message = FacebookStatus.objects.get(pk=int(request.POST['message']))
    message.status = request.POST['status']
    message.save()
    return HttpResponse('ok')

def message_post(request):
    message = FacebookStatus.objects.get(pk=int(request.POST['message']))
    graph = facebook.GraphAPI(request.user.social_auth.first().extra_data['access_token'])
    graph.put_object("me", "feed", message=message.message)
    message.publish_timestamp = datetime.datetime.now()
    message.save()
    return HttpResponse('ok')