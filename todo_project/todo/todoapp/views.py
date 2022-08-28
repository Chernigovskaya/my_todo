from django.http import Http404
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from todoapp.serializers import TODOHyperlinkedModelSerializer, ProjectHyperlinkedModelSerializer
from .models import Project, TODO


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectHyperlinkedModelSerializer
    pagination_class = ProjectLimitOffsetPagination
    # filterset_fields = ['id', 'name']

    def get_queryset(self):
        # name = self.kwargs['name']
        # return Project.objects.filter(name__contains=name)
        name = self.request.query_params.get('name', '')
        project = Project.objects.all()
        if name:
            project = project.filter(name__contains=name)
        return project


class TODOLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class TODOModelViewSet(ModelViewSet):
    queryset = TODO.objects.all()
    serializer_class = TODOHyperlinkedModelSerializer
    pagination_class = TODOLimitOffsetPagination
    filterset_fields = ['id', 'author']

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.is_active = False
            instance.save()
        except Http404:
           pass
        else:
            return Response(status=status.HTTP_204_NO_CONTENT)


