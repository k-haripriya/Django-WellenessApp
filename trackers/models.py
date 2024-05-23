from django.db import models
from datetime import date
from authapp.models import userAccount
from django.utils import timezone


class waterTracker(models.Model):
    user_id = models.ForeignKey(userAccount, on_delete = models.CASCADE,default =1)
    drank_at = models.DateField(default = date.today)

class sleepTracker(models.Model):
    user_id = models.ForeignKey(userAccount, on_delete = models.CASCADE,default =1)
    created_at = models.DateField(default = date.today)
    sleep_duration = models.DecimalField(max_digits = 3, decimal_places =0)

class moodTracker(models.Model):
    user_id = models.ForeignKey(userAccount, on_delete = models.CASCADE,default =1)
    created_at = models.DateField(default = date.today)
    mood = models.CharField(max_length=50)

class Streak(models.Model):
    user_id = models.ForeignKey(userAccount,on_delete = models.CASCADE)
    last_login = models.DateField(default=date.today())
    Streak = models.DecimalField(max_digits = 3, decimal_places = 0)
