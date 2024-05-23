from django.db import models
from hashtags.models import hashTags

class podcasts(models.Model):
    podacast_name = models.CharField(max_length = 255)
    podcast_description = models.CharField(max_length = 255)
    artist_name = models.CharField(max_length = 255)
    audio = models.CharField(max_length = 255)
    short_img = models.CharField(max_length = 255)
    long_img = models.CharField(max_length = 255)
    hashtag_id = models.ForeignKey(hashTags, on_delete = models.CASCADE)
