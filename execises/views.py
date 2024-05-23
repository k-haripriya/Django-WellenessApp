

from rest_framework.views import APIView
from .serializers import exerciseSerializer,chapterSerializer
from rest_framework import status
from rest_framework.response import Response
from .models import exercises,chapters
from hashtags.models import hashTags
from userinfoapp.models import userInfo
from execises.models import exercises
from podcasts.models import podcasts
from podcasts.serializers import podacastSerializer

class exerciseView(APIView):

    def post(self, request):
        serializer = exerciseSerializer(data=request.data)
        if serializer.is_valid():
            saved_instance = serializer.save()
            serialized_data = exerciseSerializer(saved_instance).data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class exerciseViewAll(APIView):   
    def get(self, request):
        exercises_list = exercises.objects.all()
        serializer = exerciseSerializer(exercises_list, many=True)
        return Response(serializer.data)
    
class chapterCreate(APIView):
    def post(self, request):
        serializer = chapterSerializer(data=request.data)
        if serializer.is_valid():
            saved_instance = serializer.save()
            serialized_data = chapterSerializer(saved_instance).data
            return Response(serialized_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class particularExercise(APIView):
    def get(self,request,exercise_id):
        try:
            exercise = exercises.objects.get(id=exercise_id)
        except exercises.DoesNotExist:
            return Response({"message": "Exercise not found"}, status=status.HTTP_404_NOT_FOUND)
        
        exercise_serializer = exerciseSerializer(exercise)
        associated_chapters = chapters.objects.filter(exercise_id=exercise_id)
        
        
        chapters_serializer = chapterSerializer(associated_chapters, many=True)
        
        response_data = {
            "exercise": exercise_serializer.data,
            "chapters": chapters_serializer.data
        }
        
        return Response(response_data)

class particularhashtagExercise(APIView):
    def get(self,request,hashtag_id):
        try:
            hashtag = hashTags.objects.get(id=hashtag_id)
        except hashTags.DoesNotExist:
            return Response({"message:": "Hashtag Does not Exist"}, status=status.HTTP_404_NOT_FOUND)
        
        exercises_list = exercises.objects.filter(hashtag_id=hashtag_id)
        
        serializer = exerciseSerializer(exercises_list, many=True)
        
        return Response(serializer.data)


class recommendations(APIView):
    def get(self, request, userId):
        hashTags_alter = ['depressed', 'anxious', 'doubtful', 'stressed', 'weightloss', 'weightgain', 'male', 'female', 'sleep', 'Young', 'old']

        try:
            user_info = userInfo.objects.get(user_id=userId)
        except userInfo.DoesNotExist:
            return Response({"error": "User information not found"}, status=404)

        additional_tags = []
        all_hashtags = hashTags.objects.all().values_list('hashtag_name', flat=True)

        additional_tags += [hashtag for hashtag in all_hashtags if hashtag not in hashTags_alter]


        current_mood = user_info.current_mood.lower()
        if 'depressed' in current_mood:
            additional_tags.append('depressed')
        if 'anxious' in current_mood:
            additional_tags.append('anxious')
        if 'doubtful' in current_mood:
            additional_tags.append('doubtful')

        if user_info.age < 30:
            additional_tags.append('young')
        else:
            additional_tags.append('old')

        recommended_hashtags = hashTags.objects.filter(hashtag_name__in=additional_tags).values('id', 'hashtag_name')

        results = []

        for hashtag in recommended_hashtags:
            exercises_list = exercises.objects.filter(hashtag_id=hashtag['id'])

            exercise_data = []
            for exercise in exercises_list:
                exercise_serializer = exerciseSerializer(exercise)
                exercise_data.append(exercise_serializer.data)

            results.append({
                "hashtag": {"id": hashtag['id'], "hashtag_name": hashtag['hashtag_name']},
                "exercises": exercise_data
            })

        return Response({"results": results})

class recommendPodcasts(APIView):
     def get(self, request, userId):
        hashTags_alter = ['depressed', 'anxious', 'doubtful', 'stressed', 'weightloss', 'weightgain', 'male', 'female', 'sleep', 'Young', 'old']

        try:
            user_info = userInfo.objects.get(user_id=userId)
        except userInfo.DoesNotExist:
            return Response({"error": "User information not found"}, status=404)

        additional_tags = []
        all_hashtags = hashTags.objects.all().values_list('hashtag_name', flat=True)

        additional_tags += [hashtag for hashtag in all_hashtags if hashtag not in hashTags_alter]


        current_mood = user_info.current_mood.lower()
        if 'depressed' in current_mood:
            additional_tags.append('depressed')
        if 'anxious' in current_mood:
            additional_tags.append('anxious')
        if 'doubtful' in current_mood:
            additional_tags.append('doubtful')

        if user_info.age < 30:
            additional_tags.append('young')
        else:
            additional_tags.append('old')

        recommended_hashtags = hashTags.objects.filter(hashtag_name__in=additional_tags).values('id', 'hashtag_name')

        results = []

        for hashtag in recommended_hashtags:
            podcast_list = podcasts.objects.filter(hashtag_id=hashtag['id'])

            exercise_data = []
            for exercise in podcast_list:
                exercise_serializer = podacastSerializer(exercise)
                exercise_data.append(exercise_serializer.data)

            results.append({
                "hashtag": {"id": hashtag['id'], "hashtag_name": hashtag['hashtag_name']},
                "podcasts": exercise_data
            })

        return Response({"results": results})
     
class deleteExercise(APIView):
    def delete(self, request, exercise_id):
        try:
            exercise = exercises.objects.get(pk=exercise_id)
            exercise.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except exercises.DoesNotExist:
            return Response({"message": "Exercise not found"}, status=status.HTTP_404_NOT_FOUND)
        
class DeleteChapter(APIView):
    def delete(self, request, chapter_id):
        try:
            chapter = chapters.objects.get(pk=chapter_id)
            chapter.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except chapters.DoesNotExist:
            return Response({"message": "Chapter not found"}, status=status.HTTP_404_NOT_FOUND)
