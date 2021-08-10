import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from Orgs.models import Tip, TipStructure, Tie, TipQuestion, TieQuestion, TipFact, TieFact, Display, DisplayOrder, \
    DisplayCollection, TieStructure


# class TipNode(DjangoObjectType):
#     class Meta:
#         model = Tip
#         filter_fields = ['structure']
#         interfaces = (relay.Node, )
#
#
# class TipStructureNode(DjangoObjectType):
#     class Meta:
#         model = TipStructure
#         filter_fields = []
#         interfaces = (relay.Node, )
#
#
# class TieNode(DjangoObjectType):
#     class Meta:
#         model = Tie
#         filter_fields = []
#         interfaces = (relay.Node, )
#
#
# class TieStructureNode(DjangoObjectType):
#     class Meta:
#         model = TieStructure
#         filter_fields = []
#         interfaces = (relay.Node, )
#
#
# class TipQuestionNode(DjangoObjectType):
#     class Meta:
#         model = TipQuestion
#         filter_fields = []
#         interfaces = (relay.Node, )
#
#
# class TieQuestionNode(DjangoObjectType):
#     class Meta:
#         model = TieQuestion
#         filter_fields = []
#         interfaces = (relay.Node, )
#
#
# class TipFactNode(DjangoObjectType):
#     class Meta:
#         model = TipFact
#         filter_fields = []
#         interfaces = (relay.Node, )
#
#
# class TieFactNode(DjangoObjectType):
#     class Meta:
#         model = TieFact
#         filter_fields = []
#         interfaces = (relay.Node, )
#
#
# class DisplayNode(DjangoObjectType):
#     class Meta:
#         model = Display
#         filter_fields = []
#         interfaces = (relay.Node, )
#
#
# class DisplayOrderNode(DjangoObjectType):
#     class Meta:
#         model = DisplayOrder
#         filter_fields = []
#         interfaces = (relay.Node, )
#
#
# class DisplayCollectionNode(DjangoObjectType):
#     class Meta:
#         model = DisplayCollection
#         filter_fields = []
#         interfaces = (relay.Node, )
#




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
#         model = DisplayCollection
#         fields = '__all__'
#
#
# class DisplayOrderType(DjangoObjectType):
#     class Meta:
#         model = DisplayOrder
#         fields = '__all__'


# class Query(graphene.ObjectType):
#     tip = relay.Node.Field(TipNode)
#     tips = DjangoFilterConnectionField(TipNode)
#
#     tie = relay.Node.Field(TieNode)
#     ties = DjangoFilterConnectionField(TieNode)
#
#     tip_structure = relay.Node.Field(TipStructureNode)
#     tip_structures = DjangoFilterConnectionField(TipStructureNode)
#
#     tie_structure = relay.Node.Field(TieStructureNode)
#     tie_structures = DjangoFilterConnectionField(TieStructureNode)
#
#     tip_question = relay.Node.Field(TipQuestionNode)
#     tip_questions = DjangoFilterConnectionField(TipQuestionNode)
#
#     tie_question = relay.Node.Field(TieQuestionNode)
#     tie_questions = DjangoFilterConnectionField(TieQuestionNode)
#
#     tip_fact = relay.Node.Field(TipFactNode)
#     tip_facts = DjangoFilterConnectionField(TipFactNode)
#
#     tie_fact = relay.Node.Field(TieFactNode)
#     tie_facts = DjangoFilterConnectionField(TieFactNode)
#
#     display = relay.Node.Field(DisplayNode)
#     displays = DjangoFilterConnectionField(DisplayNode)
#
#     display_collection = relay.Node.Field(DisplayCollectionNode)
#     display_collections = DjangoFilterConnectionField(DisplayCollectionNode)


class Mutation(graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
