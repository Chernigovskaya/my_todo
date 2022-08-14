from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet

from todoapp.serializers import TODOHyperlinkedModelSerializer, ProjectHyperlinkedModelSerializer
from .models import Project, TODO


class ProjectModelViewSet(ModelViewSet):
    #renderer_classes = [JSONRenderer]
    queryset = Project.objects.all()
    serializer_class = ProjectHyperlinkedModelSerializer


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOHyperlinkedModelSerializer

