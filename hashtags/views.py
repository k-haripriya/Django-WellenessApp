from rest_framework.views import APIView
from .serializers import hashtagsSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import hashTags

class hashtagCreate(APIView):

    def post(self, request):
        serializer = hashtagsSerializer(data=request.data)
        if serializer.is_valid():
            saved_instance = serializer.save()
            serialized_data = hashtagsSerializer(saved_instance).data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class HashtagList(APIView):
    def get(self, request):
        hashtags = hashTags.objects.all()
        serializer = hashtagsSerializer(hashtags, many=True)
        return Response(serializer.data)
    
class DeleteHashtag(APIView):
    def delete(self, request, hashtag_id):
        try:
            hashtag = hashTags.objects.get(pk=hashtag_id)
            hashtag.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except hashTags.DoesNotExist:
            return Response({"message": "Hashtag not found"}, status=status.HTTP_404_NOT_FOUND)