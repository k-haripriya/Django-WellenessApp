from rest_framework.views import APIView
from .serializers import waterTrackerSerializer,sleepTrackerSerializer,moodTrackerSerializer,StreakSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import waterTracker,moodTracker,sleepTracker,Streak
from datetime import datetime, date,timedelta
from django.utils import timezone
from authapp.models import userAccount

class watertrackerView(APIView):

    def post(self, request):
        serializer = waterTrackerSerializer(data= request.data)
        if serializer.is_valid():
            saved_instance = serializer.save()
            serialized_data = waterTrackerSerializer(saved_instance).data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class getWaterTracker(APIView):
    def get(self,request,userId):
        today_date = date.today()
        water_count = waterTracker.objects.filter(user_id=userId, drank_at=today_date).count()

        return Response({"count":water_count}, status=status.HTTP_200_OK)
    
class SleepTrackerView(APIView):
    def post (self,request):
        serializer = sleepTrackerSerializer(data= request.data)
        if serializer.is_valid():
            saved_instance = serializer.save()
            serialized_data = sleepTrackerSerializer(saved_instance).data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class getSleepAverage(APIView):
    def get(self,request,userId):
        today_date = date.today()
    
        three_days_ago = today_date - timedelta(days=3)
        
        sleep_records = sleepTracker.objects.filter(user_id=userId, created_at__gte=three_days_ago, created_at__lte=today_date)
        
        total_sleep_duration = sum(record.sleep_duration for record in sleep_records)
        count = sleep_records.count()
        
        if count > 0:
            average_sleep_duration = total_sleep_duration / count
        else:
            average_sleep_duration = 0
        
        return Response({"average":average_sleep_duration}, status=status.HTTP_200_OK)
    
class SleepEntryExists(APIView):
    def get(self, request,userId):
        today_date = date.today()
        
        today_entries_exist = sleepTracker.objects.filter(created_at=today_date , user_id =userId).exists()
        
        return Response({"today_entries_exist": today_entries_exist}, status=status.HTTP_200_OK)
    
class MoodTrackerView(APIView):
    def post (self,request):
        serializer = moodTrackerSerializer(data= request.data)
        if serializer.is_valid():
            saved_instance = serializer.save()
            serialized_data = moodTrackerSerializer(saved_instance).data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class getMoodTracker(APIView):
    def get(self,request,userId):
        today_date = date.today()
        mood = moodTracker.objects.filter(user_id=userId, created_at=today_date)
        serializer = moodTrackerSerializer(mood, many=True)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

class postStreak(APIView):
    def post(self,request):
        serializer = StreakSerializer(data= request.data)
        if serializer.is_valid():
            saved_instance = serializer.save()
            serialized_data = StreakSerializer(saved_instance).data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class updateStreaks(APIView):
    def put(self, request, userId):
        try:
            streak = Streak.objects.get(user_id=userId)
            yesterday = timezone.now() - timedelta(days=1)
            today = timezone.now().date()
            yesterday = yesterday.date()

            if streak.last_login:
                last_login_date = streak.last_login
                if last_login_date == yesterday:
                    streak.Streak += 1
                elif last_login_date != today:
                    streak.Streak = 1
                

            streak.last_login = timezone.now().date()
            streak.save()

            serializer = StreakSerializer(streak)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Streak.DoesNotExist:
            return Response("Streak record does not exist", status=status.HTTP_404_NOT_FOUND)
        except userAccount.DoesNotExist:
            return Response("User does not exist", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(f"An error occurred: {str(e)}", status=status.HTTP_500_INTERNAL_SERVER_ERROR)