from django.db import models
from authapp.models import userAccount

class userInfo(models.Model):
    user = models.ForeignKey(userAccount, on_delete = models.CASCADE)
    goal = models.CharField(max_length = 255)
    gender = models.CharField(max_length = 255)
    age = models.DecimalField(max_digits =2, decimal_places =0)
    weight = models.DecimalField(max_digits =5, decimal_places =2)
    current_mood = models.CharField(max_length = 255)
    past_medical_help = models.BooleanField(default=False)
    physical_stress = models.BooleanField(default = True)
    sleep_quality = models.CharField(max_length = 255)
    medications = models.CharField(max_length = 255)
    stress_level =  models.DecimalField(max_digits =1 , decimal_places = 0)
    



    
    



