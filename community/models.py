from django.db import models
from authapp.models import userAccount
from datetime import date

class community(models.Model):
    community_name = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    admin_name = models.CharField(max_length = 255)
    created_on = models.DateField(default = date.today)

class communityMembers(models.Model):
    community_id = models.ForeignKey(community,on_delete = models.CASCADE)
    user_id = models.ForeignKey(userAccount, on_delete = models.CASCADE)

class communityMessages(models.Model):
    message = models.CharField(max_length = 255)
    fromUser = models.ForeignKey(userAccount,on_delete = models.CASCADE,related_name='sent_messages')
    toUser = models.ForeignKey(userAccount,on_delete = models.CASCADE,related_name='received_messages')
    isReply = models.BooleanField(default = False)
    repliedTo = models.ForeignKey(userAccount,on_delete = models.CASCADE,null = True, blank = True)
    time = models.DateField(null = True)
    community_id = models.ForeignKey(community,on_delete = models.CASCADE)