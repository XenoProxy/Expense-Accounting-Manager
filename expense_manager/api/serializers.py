from rest_framework import serializers
from django.contrib.auth.models import UserManager
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.utils.six import BytesIO

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

# сериализация объектов
json = JSONRenderer().render(serializer.data)
json

# десериализация объектов
stream = BytesIO(json)
data = JSONParser().parse(stream)
# затем мы сохраняем эти нативные типы данных в словарь валидных данных.
serializer = CategorySerializer(data=data)
serializer.is_valid()
# True
serializer.validated_data