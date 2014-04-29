from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from fbposter.models import FacebookStatus
import facebook
import datetime

class Command(BaseCommand):
    args = ''
    help = 'Gets fresh messages from Reddit'

    def handle(self, *args, **options):
        if len(args) < 1:
            self.stdout.write('Usage: ./manage.py facebook_post ')
            return
