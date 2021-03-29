from rest_framework import serializers
from .models import EdgeType, Edge, Node, NodeType, ValidEdge

# Basic write-ready serializers


class EdgeTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EdgeType
        fields = '__all__'


class EdgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Edge
        fields = '__all__'


class NodeTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = NodeType
        fields = '__all__'


class NodeSerializer(serializers.ModelSerializer):

    # def to_representation(self, instance):
    #     if isinstance(instance, Org):
    #         return OrgSerializer(instance=instance).data
    #     elif isinstance(instance, Position):
    #         return PositionSerializer(instance=instance).data
    #     else:
    #         return PersonSerializer(instance=instance).data

    class Meta:
        model = Node
        fields = '__all__'


class ValidEdgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ValidEdge
        fields = '__all__'