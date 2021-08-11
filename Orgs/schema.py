import graphene
from graphene import relay, Interface
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from Orgs.models import Tip, TipStructure, Tie, Question, Fact,\
    Display, DisplayOrder, DisplayCollection, TieStructure, Fact





class TipNode(DjangoObjectType):
    class Meta:
        model = Tip
        filter_fields = ['structure']
        interfaces = (relay.Node, )


class TipStructureNode(DjangoObjectType):
    class Meta:
        model = TipStructure
        filter_fields = []
        interfaces = (relay.Node, )


class TieNode(DjangoObjectType):
    class Meta:
        model = Tie
        filter_fields = []
        interfaces = (relay.Node, )


class TieStructureNode(DjangoObjectType):
    class Meta:
        model = TieStructure
        filter_fields = []
        interfaces = (relay.Node, )


class QuestionNode(DjangoObjectType):
    class Meta:
        model = Question
        filter_fields = []
        interfaces = (relay.Node, )


# class FactData(graphene.Union):
#     class Meta:
#         types = (graphene.String, graphene.Int, graphene.Float, graphene.Date)


class FactNode(DjangoObjectType):
    class Meta:
        model = Fact
        fields = ("question", "dat", "sources", "check", "qu")
        filter_fields = []
        interfaces = (relay.Node, )

    dat = graphene.String()
    check = graphene.String()
    # qu = graphene.List(TipNode)
    qu = DjangoFilterConnectionField(TipNode)

    def resolve_dat(instance, info, **kwargs):
        return instance.data

    def resolve_check(instance, info, **kwargs):
        return instance.show_check("It is working")

    def resolve_qu(instance, info, **kwargs):
        return instance.show_q()



class DisplayNode(DjangoObjectType):
    class Meta:
        model = Display
        filter_fields = []
        interfaces = (relay.Node, )


class DisplayOrderNode(DjangoObjectType):
    class Meta:
        model = DisplayOrder
        filter_fields = []
        interfaces = (relay.Node, )


class DisplayCollectionNode(DjangoObjectType):
    class Meta:
        model = DisplayCollection
        filter_fields = []
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
#         model = DisplayCollection
#         fields = '__all__'
#
#
# class DisplayOrderType(DjangoObjectType):
#     class Meta:
#         model = DisplayOrder
#         fields = '__all__'


class Query(graphene.ObjectType):
    tip = relay.Node.Field(TipNode)
    tips = DjangoFilterConnectionField(TipNode)

    tie = relay.Node.Field(TieNode)
    ties = DjangoFilterConnectionField(TieNode)

    tip_structure = relay.Node.Field(TipStructureNode)
    tip_structures = DjangoFilterConnectionField(TipStructureNode)

    tie_structure = relay.Node.Field(TieStructureNode)
    tie_structures = DjangoFilterConnectionField(TieStructureNode)

    question = relay.Node.Field(QuestionNode)
    questions = DjangoFilterConnectionField(QuestionNode)

    fact = relay.Node.Field(FactNode)
    facts = DjangoFilterConnectionField(FactNode)

    display = relay.Node.Field(DisplayNode)
    displays = DjangoFilterConnectionField(DisplayNode)

    display_collection = relay.Node.Field(DisplayCollectionNode)
    display_collections = DjangoFilterConnectionField(DisplayCollectionNode)

#
# class Mutation(graphene.ObjectType):
#     pass


schema = graphene.Schema(query=Query)
