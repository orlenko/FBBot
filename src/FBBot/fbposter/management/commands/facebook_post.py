from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from fbposter.models import FacebookStatus
import facebook
import datetime

class Command(BaseCommand):
    args = ''
    help = 'Posts a message to Facebook'

    def handle(self, *args, **options):
        if len(args) < 1:
            self.stdout.write('Usage: ./manage.py facebook_post <user_email> ')
            return
        user = User.objects.get(email=args[0])
        messages = FacebookStatus.objects.filter(status='approved', publish_timestamp=None, author=user)[:1]
        if not messages:
            self.stdout.write('There are no pending messages for %s' % user)
            return
        message = messages[0]
        auth = user.social_auth.first()
        if not auth:
            self.stdout.write('User %s is not authenticated with Facebook' % user)
            return
        graph = facebook.GraphAPI(auth.extra_data['access_token'])
        graph.put_object("me", "feed", message=message.message)
        message.publish_timestamp = datetime.datetime.now()
        message.save()
        self.stdout.write('Message posted successfully on behalf of %s: %s' % (user, message))