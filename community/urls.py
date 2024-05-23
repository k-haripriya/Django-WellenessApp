from django.urls import path
from .views import communityCreate,communityMemberCreate,communityMessageCreate,communityGetMessages,getMyCommunity,getAllCommunity,getCommunityMembers

urlpatterns = [
    path('create/',communityCreate.as_view(),name="community-create"),
    path('enroll/',communityMemberCreate.as_view(), name="enroll-members"),
    path('sendMessage/',communityMessageCreate.as_view(),name="send_message"),
    path('getMessages/<int:communityId>',communityGetMessages.as_view(),name="get-messages"),
    path('getMyCommunity/<int:userId>',getMyCommunity.as_view(),name="get-my-community"),
    path('list/',getAllCommunity.as_view(),name="get-all-community"),
    path('getMembers/<int:communityId>',getCommunityMembers.as_view(),name='community-members')
    
]
