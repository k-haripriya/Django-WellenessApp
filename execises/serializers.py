from rest_framework import serializers
from .models import exercises,chapters

class exerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = exercises
        fields = '__all__'

class chapterSerializer(serializers.ModelSerializer):
    class Meta:
        model = chapters
        fields = '__all__'