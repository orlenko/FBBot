from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class FacebookStatus(models.Model):

    class Meta:
        verbose_name_plural = 'Facebook Statuses'
        ordering = ['publish_timestamp']

    STATUS = (
        ('draft', 'Draft'),
        ('approved', 'Approved'),
    )
    status = models.CharField(max_length=255, choices=STATUS, default=STATUS[0][0])
    publish_timestamp = models.DateTimeField(null=True, blank=True)
    author = models.ForeignKey(User)
    message = models.TextField(max_length=255)
    link = models.URLField(null=True, blank=True)

    def __unicode__(self):
        return self.message


class Subreddit(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s (#%s)' % (self.name, self.id)


class UserSubreddit(models.Model):
    user = models.ForeignKey(User)
    subreddit = models.ForeignKey(Subreddit)

    def __unicode__(self):
        try:
            return '%s - %s' % (self.user, self.subreddit)
        except:
            return '%s - %s' % (self.user_id, self.subreddit_id)
