from rest_framework import serializers
from .models import EdgeType, Edge, Node, NodeType, ValidEdgeType, Display, DisplaySet, DisplayOrder


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


class WorkingNodeSerializer(serializers.ModelSerializer):
    node_type = NodeTypeSerializer(read_only=True)

    class Meta:
        model = Node
        fields = '__all__'


class ValidEdgeTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = ValidEdgeType
        fields = '__all__'


class LeftValidEdgeTypeSerializer(serializers.ModelSerializer):
    edge_type = EdgeTypeSerializer(read_only=True)
    left_node_type = NodeTypeSerializer(read_only=True)

    class Meta:
        model = ValidEdgeType
        fields = '__all__'


class RightValidEdgeTypeSerializer(serializers.ModelSerializer):
    edge_type = EdgeTypeSerializer(read_only=True)
    right_node_type = NodeTypeSerializer(read_only=True)

    class Meta:
        model = ValidEdgeType
        fields = '__all__'


class LeftEdgeSerializer(serializers.ModelSerializer):
    left_node = NodeSerializer(read_only=True)

    class Meta:
        model = Edge
        fields = '__all__'


class RightEdgeSerializer(serializers.ModelSerializer):
    right_node = NodeSerializer(read_only=True)

    class Meta:
        model = Edge
        fields = '__all__'


class NodeRelsSerializer(serializers.ModelSerializer):
    left_edges = EdgeSerializer(many=True, read_only=True)
    right_edges = EdgeSerializer(many=True, read_only=True)
    left_edges__left_node = NodeSerializer(many=True, read_only=True)

    class Meta:
        model = Node
        fields = '__all__'


class DisplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = Display
        fields = '__all__'


class DisplaySetSerializer(serializers.ModelSerializer):

    class Meta:
        model = DisplaySet
        fields = '__all__'


class DisplayOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = DisplayOrder
        fields = '__all__'
