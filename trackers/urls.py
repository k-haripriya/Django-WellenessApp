from django.urls import path,include
from .views import watertrackerView,getWaterTracker,SleepTrackerView,MoodTrackerView,getMoodTracker,getSleepAverage,updateStreaks,postStreak,SleepEntryExists

urlpatterns = [
    path('addwater/',watertrackerView.as_view(),name="water-tracker"),
    path('getwater/<int:userId>',getWaterTracker.as_view(),name="get-water"),
    path('tracksleep/',SleepTrackerView.as_view(),name="sleep-tracker"),
    path('trackmood/',MoodTrackerView.as_view(),name="mood-tracker"),
    path('getMood/<int:userId>',getMoodTracker.as_view(),name="get-mood"),
    path('getAverageSleep/<int:userId>',getSleepAverage.as_view(),name="get-sleep-average"),
    path('streak/<int:userId>',updateStreaks.as_view(),name="streaks"),
    path('addstreak/',postStreak.as_view(),name="post-streak"),
    path('checksleep/<int:userId>',SleepEntryExists.as_view(),name='sleep-entry')
]
