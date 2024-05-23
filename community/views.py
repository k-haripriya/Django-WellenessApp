from rest_framework.views import APIView
from .serializers import communitySerializer,communityMenmbersSerializer,communityMessagesSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import community,communityMembers,communityMessages
from authapp.models import userAccount

class communityCreate(APIView):

    def post(self, request):
        serializer = communitySerializer(data= request.data)
        if serializer.is_valid():
            saved_instance = serializer.save()
            serialized_data = communitySerializer(saved_instance).data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class communityMemberCreate(APIView):

    def post(self, request):
        serializer = communityMenmbersSerializer(data= request.data)
        if serializer.is_valid():
            saved_instance = serializer.save()
            serialized_data = communityMenmbersSerializer(saved_instance).data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class communityMessageCreate(APIView):

    def post(self, request):
        serializer = communityMessagesSerializer(data= request.data)
        if serializer.is_valid():
            saved_instance = serializer.save()
            serialized_data = communityMessagesSerializer(saved_instance).data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class communityGetMessages(APIView):

    def get(self, request, communityId):
        messages_list = communityMessages.objects.filter(community_id = communityId )
        serializer = communityMessagesSerializer(messages_list, many=True)
        return Response(serializer.data)

class getMyCommunity(APIView):

    def get(self,request, userId):
        community_ids = communityMembers.objects.filter(user_id= userId).values_list('community_id', flat=True)

        communities = community.objects.filter(id__in=community_ids)
        serializer = communitySerializer(communities, many=True)

        return Response(serializer.data)
    
class getAllCommunity(APIView):

    def get(self,request):

        communities = community.objects.all()
        serializer = communitySerializer(communities, many=True)

        return Response(serializer.data)
    
class getCommunityMembers(APIView):
    def get(self,request,communityId):
        community_members = communityMembers.objects.filter(community_id=communityId)
        member_ids = community_members.values_list('user_id', flat=True)

       
        users = userAccount.objects.filter(id__in=member_ids)

        
        return Response(users.values(), status=status.HTTP_200_OK)



    
