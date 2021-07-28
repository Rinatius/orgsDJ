import graphene
from graphene_django import DjangoObjectType

from Orgs.models import Node, NodeSchema


class NodeType(DjangoObjectType):
    class Meta:
        model = Node
        fields = '__all__'


class NodeSchemaType(DjangoObjectType):
    class Meta:
        model = NodeSchema
        fields = '__all__'


class Query(graphene.ObjectType):
    all_nodes = graphene.List(NodeType)
    node_schema_by_name = graphene.Field(NodeSchemaType, name=graphene.String(required=True))

    def resolve_all_nodes(root, info):
        # We can easily optimize query count in the resolve method
        return Node.objects.select_related("schema").all()

    def resolve_node_schema_by_name(root, info, name):
        try:
            return NodeSchema.objects.get(name=name)
        except NodeSchema.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)
