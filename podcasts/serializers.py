from rest_framework import serializers
from .models import podcasts

class podacastSerializer(serializers.ModelSerializer):
    class Meta:
        model = podcasts
        fields = '__all__'