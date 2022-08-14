from rest_framework.serializers import HyperlinkedModelSerializer,ModelSerializer
from rest_framework.relations import StringRelatedField

from .models import UsersTodo


class UsersModelSerializer(ModelSerializer):

    class Meta:
        model = UsersTodo
        fields = ['id', 'username', 'first_name', 'last_name', 'email']
        #exclude = ['email'] исключить
