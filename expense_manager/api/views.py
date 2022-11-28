# Для создания эндпоинта только для чтения, который возвращал бы список пользователей
from rest_framework import generics
from . import serializers
from rest_framework import viewsets
from django.contrib.auth.models import User


from serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserSerializer


# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = serializers.UserSerializerrender

# # Create your views here.
