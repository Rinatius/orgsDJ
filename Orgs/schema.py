import graphene
from graphene import relay
from graphene_django import DjangoObjectType

from Orgs.models import Node, NodeSchema, Edge, EdgeSchema, EdgeSchema, Display, DisplaySet, DisplayOrder


class NodeType(DjangoObjectType):
    class Meta:
        model = Node
        fields = '__all__'


class NodeSchemaType(DjangoObjectType):
    class Meta:
        model = NodeSchema
        fields = '__all__'


class EdgeType(DjangoObjectType):
    class Meta:
        model = Edge
        fields = '__all__'


class EdgeSchemaType(DjangoObjectType):
    class Meta:
        model = EdgeSchema
        fields = '__all__'


class ValidEdgeType(DjangoObjectType):
    class Meta:
        model = EdgeSchema
        fields = '__all__'


class DisplayType(DjangoObjectType):
    class Meta:
        model = Display
        fields = '__all__'


class DisplaySetType(DjangoObjectType):
    class Meta:
        model = DisplaySet
        fields = '__all__'


class DisplayOrderType(DjangoObjectType):
    class Meta:
        model = DisplayOrder
        fields = '__all__'


class Query(graphene.ObjectType):
    all_nodes = graphene.List(NodeType)
    node_schema_by_name = graphene.Field(NodeSchemaType, name=graphene.String(required=True))

    def resolve_all_nodes(root, info):
        # We can easily optimize query count in the resolve method
        return Node.objects.all()

    # def resolve_node_schema_by_name(root, info, name):
    #     try:
    #         return NodeSchema.objects.get(name=name)
    #     except NodeSchema.DoesNotExist:
    #         return None


schema = graphene.Schema(query=Query)
