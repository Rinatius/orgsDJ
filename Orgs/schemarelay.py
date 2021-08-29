import graphene, graphene_django
from graphene import relay, Interface
from graphene_django import DjangoObjectType, DjangoConnectionField
from graphene_django.filter import DjangoFilterConnectionField

from Orgs import formats
from Orgs.models import Tip, TipStructure, Tie, Question, Fact,\
    Display, DisplayOrder, DisplayCollection, TieStructure, Fact


class QuestionNode(DjangoObjectType):
    class Meta:
        model = Question
        filter_fields = []
        interfaces = (relay.Node, )



class FactInterface(relay.Node):

    question = graphene.Field(QuestionNode)

    sources = DjangoFilterConnectionField(lambda: TipNode)

    @classmethod
    def resolve_type(cls, instance, info):
        if instance.question.input_format == formats.INT_FORMAT:
            return IntFactNode
        elif instance.question.input_format == formats.FLOAT_FORMAT:
            return FloatFactNode
        elif instance.question.input_format == formats.DATE_FORMAT:
            return DateFactNode
        else:
            return TextFactNode


class IntFactNode(DjangoObjectType):
    class Meta:
        model = Fact
        fields = ("data", "response_int")
        interfaces = (FactInterface,)

    data = graphene.Int()

    def resolve_data(instance, info, **kwargs):
        return instance.get_data()


class FloatFactNode(DjangoObjectType):
    class Meta:
        model = Fact
        fields = ("data", "response_float")
        interfaces = (FactInterface,)

    data = graphene.Float()

    def resolve_data(instance, info, **kwargs):
        return instance.get_data()


class TextFactNode(DjangoObjectType):
    class Meta:
        model = Fact
        fields = ("data", "response_text")
        interfaces = (FactInterface,)

    data = graphene.String()

    def resolve_data(instance, info, **kwargs):
        return instance.get_data()


class DateFactNode(DjangoObjectType):
    class Meta:
        model = Fact
        fields = ("data", "response_date")
        interfaces = (FactInterface,)

    data = graphene.Date()

    def resolve_data(instance, info, **kwargs):
        return instance.get_data()


class FactsUnion(graphene.types.Union):
    class Meta:
        types = [DateFactNode, IntFactNode, FloatFactNode, TextFactNode]

    @classmethod
    def resolve_type(cls, instance, info):
        if instance.question.input_format == formats.INT_FORMAT:
            return IntFactNode
        elif instance.question.input_format == formats.FLOAT_FORMAT:
            return FloatFactNode
        elif instance.question.input_format == formats.DATE_FORMAT:
            return DateFactNode
        else:
            return TextFactNode


class FactConnection(relay.Connection):
    class Meta:
        node = FactsUnion


class FactInterfaceConnection(relay.Connection):
    class Meta:
        node = FactInterface


class TipNode(DjangoObjectType):
    class Meta:
        model = Tip
        fields = ['name', 'structure']
        filter_fields = ['structure']
        interfaces = (relay.Node, )

    formatted_facts = relay.ConnectionField(FactInterfaceConnection)

    def resolve_formatted_facts(instance, info, **kwargs):
        return instance.facts.all()


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


# class FactData(graphene.Union):
#     class Meta:
#         types = (graphene.String, graphene.Int, graphene.Float, graphene.Date)



# class FactNode(DjangoObjectType):
#     class Meta:
#         model = Fact
#         fields = ("question", "dat", "sources", "check", "qu")
#         filter_fields = []
#         interfaces = (relay.Node, )
#
#     dat = graphene.String()
#     check = graphene.String()
#     # qu = graphene.List(TipNode)
#     qu = DjangoFilterConnectionField(TipNode)
#
#     def resolve_dat(instance, info, **kwargs):
#         return instance.data
#
#     def resolve_check(instance, info, **kwargs):
#         return instance.show_check("It is working")
#
#     def resolve_qu(instance, info, **kwargs):
#         return instance.show_q()



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

    # fact = relay.Node.Field(FactInterface)
    # facts = DjangoFilterConnectionField(FactInterface)

    display = relay.Node.Field(DisplayNode)
    displays = DjangoFilterConnectionField(DisplayNode)

    display_collection = relay.Node.Field(DisplayCollectionNode)
    display_collections = DjangoFilterConnectionField(DisplayCollectionNode)

#
# class Mutation(graphene.ObjectType):
#     pass


schema = graphene.Schema(query=Query, types=[IntFactNode,
                                             TextFactNode,
                                             DateFactNode,
                                             FloatFactNode,
                                             QuestionNode,
                                             FactInterface,
                                             TipNode,
                                             TipStructureNode])
