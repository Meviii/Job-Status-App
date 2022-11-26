from django.contrib import admin
from django.urls import path, include

from .views import AuthApiView, UserApiView, SingleUserApiView,home, api_auth, LogoutApiView

urlpatterns = [
    path('', home),
    path('auth/', AuthApiView.as_view()),
    path('user/', UserApiView.as_view()),
    path('user/<int:pk>/', SingleUserApiView.as_view()),
    path('auth/logout/', LogoutApiView.as_view()),
]
