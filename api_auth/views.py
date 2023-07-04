from rest_framework import generics
from rest_framework.response import Response

from .serializers import UserSerializer
from django.contrib.auth.models import User

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer