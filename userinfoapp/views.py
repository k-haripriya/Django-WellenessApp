# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import userInfo
from authapp.models import userAccount
from .serializers import UserInfoSerializer
from authapp.serializers import UserCreateSerializer


class UserInfoCreate(APIView):


    def post(self, request, format=None):
        
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserInfoGet(APIView):

    def get(self,request,userId):
       

        userInfo_list = userInfo.objects.filter(user=userId)
        userInfo_serializer = UserInfoSerializer(userInfo_list)

        return Response({"info":userInfo_serializer.data},status=status.HTTP_200_OK)

