from rest_framework.mixins import UpdateModelMixin, ListModelMixin, RetrieveModelMixin
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.viewsets import GenericViewSet

from .models import UsersTodo
from .serializers import UsersModelSerializer


class UsersModelViewSet(UpdateModelMixin, ListModelMixin, RetrieveModelMixin, GenericViewSet):

    queryset = UsersTodo.objects.all()
    serializer_class = UsersModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
