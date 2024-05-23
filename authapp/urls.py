from django.urls import path
from .views import authenticate_user_view,UserFullNameAPIView

urlpatterns = [
    path('login/',authenticate_user_view, name="authenticate-user"),
    path('name/<int:pk>',UserFullNameAPIView.as_view(),name="name-user")
]