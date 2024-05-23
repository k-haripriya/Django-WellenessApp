from django.urls import path,include
from .views import hashtagCreate,HashtagList,DeleteHashtag

urlpatterns = [
    path("create/", hashtagCreate.as_view(), name="hastag-create"),
    path("list/", HashtagList.as_view(), name="hashtag-list"),
    path("del/<int:hashtag_id>",DeleteHashtag.as_view(),name='delete-hashtag')
]
