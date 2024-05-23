from django.db import models
from hashtags.models import hashTags

class exercises(models.Model):
    exercise_name = models.CharField(max_length = 255)
    difficulty = models.CharField(max_length = 255)
    no_of_chapters = models.DecimalField(max_digits =2, decimal_places =0)
    duration = models.DecimalField(max_digits =3, decimal_places =0)
    repeat = models.DecimalField(max_digits =2, decimal_places =0)
    calories = models.DecimalField(max_digits =3, decimal_places =0)
    hashtag_id = models.ForeignKey(hashTags, on_delete = models.CASCADE)
    short_img = models.CharField(max_length = 255,null=True,blank=True)
    long_img = models.CharField(max_length = 255,null=True,blank=True)
    des = models.CharField(max_length = 255,default='')

class chapters(models.Model):
    chapter_name = models.CharField(max_length = 255)
    video = models.CharField(max_length = 1000)
    exercise_id = models.ForeignKey(exercises, on_delete = models.CASCADE)
    profile = models.CharField(max_length=1000,default='')
