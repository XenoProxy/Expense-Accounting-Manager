from rest_framework import serializers
from django.contrib.auth.models import UserManager


from models import Category


# ссылочная связь считается более правильной при проектировании API
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
            model = UserManager
            fields = ('url', 'username', 'email')

class CategorySerializer(serializers.Serializer):
    type = serializers.CharField(max_length=100)

serializer = CategorySerializer(Category.category)
serializer.data
