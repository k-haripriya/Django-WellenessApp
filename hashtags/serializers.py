from rest_framework import serializers
from .models import hashTags

class hashtagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = hashTags
        fields = ['id', 'hashtag_name']
    
