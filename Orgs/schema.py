import graphene, graphene_django
from graphene import relay, Interface
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField

from Orgs import formats
from Orgs.models import Tip, TipStructure, Tie, Question, Fact,\
    Display, DisplayOrder, DisplayCollection, TieStructure, Fact


class QuestionNode(DjangoObjectType):
    class Meta:
        model = Question
        filter_fields = []


class FactInterface(Interface):
    question = relay.Node.Field(QuestionNode)
    #sources = DjangoFilterConnectionField(TipNode)


class IntFactNode(DjangoObjectType):
    class Meta:
        model = Fact
        fields = ("data", )
        interfaces = (FactInterface, )

    data = graphene.Int()

    def resolve_data(instance, info, **kwargs):
        return instance.get_data()


class FloatFactNode(DjangoObjectType):
    class Meta:
        model = Fact
        fields = ("data",)
        interfaces = (FactInterface, )

    data = graphene.Float()

    def resolve_data(instance, info, **kwargs):
        return instance.get_data()


class TextFactNode(DjangoObjectType):
    class Meta:
        model = Fact
        fields = ("data",)
        interfaces = (FactInterface, )

    data = graphene.String()

    def resolve_data(instance, info, **kwargs):
        return instance.get_data()


class DateFactNode(DjangoObjectType):
    class Meta:
        model = Fact
        fields = ("data",)
        interfaces = (relay.Node, FactInterface)

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


class TipNode(DjangoObjectType):
    class Meta:
        model = Tip
        filter_fields = ['structure']
        interfaces = (relay.Node, )

    formatted_facts = graphene.List(FactsUnion)

    def resolve_data(instance, info, **kwargs):
        return instance.facts


class TipStructureNode(DjangoObjectType):
    class Meta:
        model = TipStructure
        filter_fields = []


class TieNode(DjangoObjectType):
    class Meta:
        model = Tie
        filter_fields = []


class TieStructureNode(DjangoObjectType):
    class Meta:
        model = TieStructure
        filter_fields = []


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


class DisplayOrderNode(DjangoObjectType):
    class Meta:
        model = DisplayOrder
        filter_fields = []


class DisplayCollectionNode(DjangoObjectType):
    class Meta:
        model = DisplayCollection
        filter_fields = []


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
    tip = graphene.Field(TipNode, pk=graphene.Int())
    tips = graphene.List(TipNode)

    tie = graphene.Field(TieNode, pk=graphene.Int())
    ties = graphene.List(TieNode)

    tip_structure = graphene.Field(TipStructureNode, pk=graphene.Int())
    tip_structures = graphene.List(TipStructureNode)

    tie_structure = graphene.Field(TieStructureNode, pk=graphene.Int())
    tie_structures = graphene.List(TieStructureNode)

    question = graphene.Field(QuestionNode, pk=graphene.Int())
    questions = graphene.List(QuestionNode)

    # fact = relay.Node.Field(FactInterface)
    # facts = DjangoFilterConnectionField(FactInterface)

    display = graphene.Field(DisplayNode, pk=graphene.Int())
    displays = graphene.List(DisplayNode)

    display_collection = graphene.Field(DisplayCollectionNode, pk=graphene.Int())
    display_collections = graphene.List(DisplayCollectionNode)

    def resolve_tip(root, info, pk):
        return Tip.objects.get(pk=pk)

    def resolve_tips(root, info, **kwargs):
        return Tip.objects.all()

    def resolve_tie(root, info, pk):
        return Tie.objects.get(pk=pk)

    def resolve_ties(root, info, **kwargs):
        return Tie.objects.all()

    def resolve_tip_structure(root, info, pk):
        return TipStructure.objects.get(pk=pk)

    def resolve_tip_structures(root, info, **kwargs):
        return TipStructure.objects.all()

    def resolve_tie_structure(root, info, pk):
        return TieStructure.objects.get(pk=pk)

    def resolve_tie_structures(root, info, **kwargs):
        return TieStructure.objects.all()

    def resolve_question(root, info, pk):
        return Question.objects.get(pk=pk)

    def resolve_questions(root, info, **kwargs):
        return Question.objects.all()

    def resolve_display(root, info, pk):
        return Display.objects.get(pk=pk)

    def resolve_displays(root, info, **kwargs):
        return Display.objects.all()

    def resolve_display_collection(root, info, pk):
        return DisplayCollection.objects.get(pk=pk)

    def resolve_display_collections(root, info, **kwargs):
        return DisplayCollection.objects.all()


#
# class Mutation(graphene.ObjectType):
#     pass


schema = graphene.Schema(query=Query)
