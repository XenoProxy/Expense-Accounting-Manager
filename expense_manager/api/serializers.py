from rest_framework import serializers
from django.contrib.auth.models import User

# ссылочная связь считается более правильной при проектировании API
class UserSerializer(serializers.ModelSerializer):
    class Meta:
            model = User
            fields = ('id', 'username', 'email')

