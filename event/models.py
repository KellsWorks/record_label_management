from django.db import models

from user.models import User

class Event(models.Model):

    title = models.CharField(max_length=255, null=False)
    location = models.CharField(max_length=255, null=False)
    artist = models.ManyToManyField(User, related_name="artist")
    start_time = models.DateTimeField(null=False)
    end_time = models.DateTimeField(null=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
