from rest_framework.relations import StringRelatedField, HyperlinkedRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer

from todoapp.models import TODO, Project


class ProjectModelSerializer(ModelSerializer):
    #users = StringRelatedField(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class TODOModelSerializer(ModelSerializer):

    class Meta:
        model = TODO
        fields = ['note', 'text_note', 'author']
