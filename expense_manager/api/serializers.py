from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Category
# ссылочная связь считается более правильной при проектировании API
class UserSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'category')

class CategorySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Category
        fields = ['id', 'type', 'owner']