from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from datetime import date, timedelta
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import userAccount
from rest_framework import status

def allow_cors(view_func):
    def wrapper(request, *args, **kwargs):
        response = view_func(request, *args, **kwargs)
        response["Access-Control-Allow-Origin"] = "*"  # Allow requests from all origins
        response["Access-Control-Allow-Methods"] = "GET, POST, PUT, PATCH, DELETE, OPTIONS"  # Allow specific HTTP methods
        response["Access-Control-Allow-Headers"] = "Content-Type, Authorization"  # Allow specific headers
        return response
    return wrapper

def authenticate_superuser(email, password):
    user = authenticate(email=email, password=password)
    if user is not None and user.is_superuser:
        return user
    else:
        return None
    
def authenticate_user(email, password):
    user = authenticate(email=email, password=password)
    return user


@csrf_exempt
@allow_cors
def authenticate_user_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        if email and password:
            superuser = authenticate_superuser(email, password)
            if superuser:
                return JsonResponse({'message': 'Authentication successful', 'user_type': 'superuser', 'email': superuser.email})

            user = authenticate_user(email, password)
            if user:
                return JsonResponse({'message': 'Authentication successful', 'user_type': 'regular', 'email': user.email, 'id':user.id})
            else:
                return JsonResponse({'message': 'Authentication failed'}, status=401)
        else:
            return JsonResponse({'message': 'Invalid request body'}, status=400)
    else:
        return JsonResponse({'message': 'Only POST requests are allowed'}, status=405)
    

class UserFullNameAPIView(APIView):
    def get(self, request, pk):
        try:
            user = userAccount.objects.get(pk=pk)
            full_name = user.get_full_name()
            return Response({'full_name': full_name}, status=status.HTTP_200_OK)
        except user.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)