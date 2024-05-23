from django.urls import path,include
from .views import exerciseView,exerciseViewAll,chapterCreate,particularExercise,particularhashtagExercise,recommendations,recommendPodcasts,deleteExercise,DeleteChapter

urlpatterns = [
    path("create/", exerciseView.as_view(), name="exercise-create"),
    path("list/", exerciseViewAll.as_view(), name="exercise-list"),
    path("chapterscreate/",chapterCreate.as_view(),name="chapter-create"),
    path('list/<int:exercise_id>/', particularExercise.as_view(),name="fetch-partcular-exercises"),
    path('list/hashtagid/<int:hashtag_id>',particularhashtagExercise.as_view(),name="hash-exercise"),
    path('recommendations/<int:userId>',recommendations.as_view(),name='recommendations'),
    path('reccomendPodcasts/<int:userId>',recommendPodcasts.as_view(),name='podacst-recommnedations'),
    path('exercisedel/<int:exercise_id>',deleteExercise.as_view(),name='Delete-Exercise'),
    path('chapterdel/<int:chapter_id>',DeleteChapter.as_view(),name='chapter-del')
]
