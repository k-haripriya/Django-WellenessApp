from rest_framework import serializers
from .models import waterTracker,sleepTracker,moodTracker,Streak

class waterTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = waterTracker
        fields = '__all__'

class sleepTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = sleepTracker
        fields = '__all__'

class moodTrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = moodTracker
        fields = '__all__'

class StreakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Streak
        fields = '__all__'