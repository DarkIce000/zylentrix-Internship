from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import UserManagementAPIView, RegisterAPIView
urlpatterns = [
    path('login', obtain_auth_token),                   # default token auth by rest_framework lib
    path('users', UserManagementAPIView.as_view()),
    path('users/<str:username>', UserManagementAPIView.as_view()),
    path('register', RegisterAPIView.as_view()),
]