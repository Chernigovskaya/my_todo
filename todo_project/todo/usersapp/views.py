
from rest_framework.viewsets import ModelViewSet

from .models import UsersTodo
from .serializers import UsersModelSerializer


class UsersModelViewSet(ModelViewSet):

    queryset = UsersTodo.objects.all()
    serializer_class = UsersModelSerializer
