from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.conf import settings
from .datasources import limerick, pirozhok
from .models import FacebookStatus, Subreddit
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.http.response import HttpResponse
import facebook
import datetime
import praw
from fbposter.models import UserSubreddit
import logging


log = logging.getLogger(__name__)


def get_top_subreddits():
    retval = Subreddit.objects.all()
    if len(retval) < 20:
        retval = []
        r = praw.Reddit(user_agent='Autobot')
        for subr in r.get_popular_subreddits():
            retval.append(Subreddit.objects.create(name=subr.display_name))
    return retval


def home(request):
    auth_profider = 'Unknown'
    msgs = []
    selected_subreddits = []
    if request.user and not request.user.is_anonymous():
        selected_subreddits = [user_subreddit.subreddit for user_subreddit in request.user.usersubreddit_set.all()]
        msgs = FacebookStatus.objects.filter(status='approved', publish_timestamp=None, author=request.user)[:10]
        social_auth = request.user.social_auth.first()
        if social_auth:
            auth_provider = social_auth.provider
    path = request.path
    setting = settings.APPEND_SLASH
    reddits = {}
    top_subreddits = get_top_subreddits()
    for subreddit in top_subreddits:
        reddits[subreddit.pk] = {'subreddit': subreddit, 'selected': False}
    for subreddit in selected_subreddits:
        reddits[subreddit.pk] = {'subreddit': subreddit, 'selected': True}
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


@login_required
def configure_reddit(request):
    user = request.user
    subreddits = request.POST.getlist('subreddit')
    log.debug('Subreddits: %s' % subreddits)
    for subreddit in subreddits:
        UserSubreddit.objects.get_or_create(user=user, subreddit_id=int(subreddit))
        log.debug('Chose an existing subreddit: %s' % subreddit)
    if request.POST['subreddit_custom']:
        subreddit, _new = Subreddit.objects.get_or_create(name=request.POST['subreddit_custom'])
        log.debug('Got or created subreddit: %s' % subreddit)
        subreddits.append(str(subreddit.id)) # Subreddit IDs come to us as strings, and we don't convert them
        UserSubreddit.objects.get_or_create(user=user, subreddit=subreddit)
    for subreddit in user.usersubreddit_set.all():
        if not (str(subreddit.subreddit_id) in subreddits):
            log.debug('Deleting an unused subreddit: %s' % subreddit)
            subreddit.delete()
    return HttpResponseRedirect('/')
