from rest_framework.serializers import HyperlinkedModelSerializer,ModelSerializer


from .models import UsersTodo


class UsersModelSerializer(ModelSerializer):
    class Meta:
        model = UsersTodo
        fields = ['username', 'first_name', 'last_name', 'email']
