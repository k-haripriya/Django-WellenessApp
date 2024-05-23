from rest_framework.views import APIView

from hashtags.models import hashTags
from .serializers import podacastSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import podcasts

class podcastCreate(APIView):

    def post(self, request):
        serializer = podacastSerializer(data= request.data)
        if serializer.is_valid():
            saved_instance = serializer.save()
            serialized_data = podacastSerializer(saved_instance).data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class PodcastList(APIView):
    def get(self, request,hashtag_id):
        try:
            hashtag = hashTags.objects.get(id=hashtag_id)
        except hashTags.DoesNotExist:
            return Response({"message:": "Hashtag Does not Exist"}, status=status.HTTP_404_NOT_FOUND)
        
        podcast_list = podcasts.objects.filter(hashtag_id=hashtag_id)
        
        serializer = podacastSerializer(podcast_list, many=True)
        
        return Response(serializer.data)
    
    