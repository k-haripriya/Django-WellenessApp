from rest_framework import serializers
from .models import community,communityMembers,communityMessages

class communitySerializer(serializers.ModelSerializer):
    class Meta:
        model = community
        fields = '__all__'

class communityMenmbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = communityMembers
        fields = '__all__'

class communityMessagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = communityMessages
        fields = '__all__'