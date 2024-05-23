from django.urls import path
from .views import podcastCreate,PodcastList

urlpatterns = [
    path('create/',podcastCreate.as_view(),name = 'podcast-create'),
    path('list/<int:hashtag_id>',PodcastList.as_view(),name='podcastlist')
]
