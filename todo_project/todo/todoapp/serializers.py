from rest_framework.relations import StringRelatedField, HyperlinkedRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from todoapp.models import TODO, Project


class ProjectHyperlinkedModelSerializer(HyperlinkedModelSerializer):
    #users = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class TODOHyperlinkedModelSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = TODO
        fields = ['note', 'text_note', 'author']
