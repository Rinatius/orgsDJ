import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from Orgs.models import Tip, TipStructure, Tie, TieStructure, TieStructure, Display, DisplaySet, DisplayOrder


class TipType(DjangoObjectType):
    class Meta:
        model = Tip
        fields = '__all__'
        filter_fields = ['structure']
        interfaces = (relay.Node, )


class TipStructureType(DjangoObjectType):
    class Meta:
        model = TipStructure
        fields = '__all__'
        interfaces = (relay.Node, )


# class NodeSchemaType(DjangoObjectType):
#     class Meta:
#         model = TipStructure
#         fields = '__all__'
#
#
# class EdgeType(DjangoObjectType):
#     class Meta:
#         model = Tie
#         fields = '__all__'
#
#
# class EdgeSchemaType(DjangoObjectType):
#     class Meta:
#         model = TieStructure
#         fields = '__all__'
#
#
# class ValidEdgeType(DjangoObjectType):
#     class Meta:
#         model = TieStructure
#         fields = '__all__'
#
#
# class DisplayType(DjangoObjectType):
#     class Meta:
#         model = Display
#         fields = '__all__'
#
#
# class DisplaySetType(DjangoObjectType):
#     class Meta:
#         model = DisplaySet
#         fields = '__all__'
#
#
# class DisplayOrderType(DjangoObjectType):
#     class Meta:
#         model = DisplayOrder
#         fields = '__all__'


class Query(graphene.ObjectType):
    tip = relay.Node.Field(TipType)
    tips = DjangoFilterConnectionField(TipType)

    tip_structure = relay.Node.Field(TipStructureType)
    tip_structures = DjangoFilterConnectionField(TipStructureType)


schema = graphene.Schema(query=Query)
