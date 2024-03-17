from django.urls import include,path
from rest_framework.authtoken.views import obtain_auth_token
from .views import register
from django.contrib.auth.models import User


urlpatterns = [
    path('user/gen/token',obtain_auth_token),
    path('user/register',register),
]