# urls.py
from django.urls import path
from .views import UserInfoCreate,UserInfoGet

urlpatterns = [
    path('create/', UserInfoCreate.as_view(), name='user-info-create'),
    path('get/<int:userId>', UserInfoGet.as_view(), name='UserInfo-get')
]
