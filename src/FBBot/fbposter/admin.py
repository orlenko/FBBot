from django.contrib import admin
from .models import FacebookStatus, Subreddit, UserSubreddit


class FacebookStatusAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'author', 'status', 'publish_timestamp']
    list_editable = ['status',]
    list_filter = ['author', 'status', 'publish_timestamp']

admin.site.register(FacebookStatus, FacebookStatusAdmin)

admin.site.register(Subreddit)
admin.site.register(UserSubreddit)