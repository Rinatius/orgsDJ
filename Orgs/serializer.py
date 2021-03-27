from rest_framework import serializers
from .models import Org, Person, Position, PositionType, EdgeType, Edge, Node

chronoModelFields = ("id",
                     "description",
                     "start_year",
                     "start_month",
                     "start_day",
                     "end_year",
                     "end_month",
                     "end_day")


# Basic write-ready serializers

class OrgSerializer(serializers.ModelSerializer):

    class Meta:
        model = Org
        fields = '__all__'
        depth = 2


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'


class PositionTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = PositionType
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = '__all__'


class PositionReadableSerializer(serializers.ModelSerializer):

    name = PositionTypeSerializer(many=False, read_only=True)
    orgs = OrgSerializer(many=True, read_only=True)

    class Meta:
        model = Position
        fields = '__all__'


class EdgeTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = EdgeType
        fields = '__all__'


class EdgeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Edge
        fields = '__all__'


class NodeSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        if isinstance(instance, Org):
            return OrgSerializer(instance=instance).data
        elif isinstance(instance, Position):
            return PositionSerializer(instance=instance).data
        else:
            return PersonSerializer(instance=instance).data

    class Meta:
        model = Node
        fields = '__all__'

# class EmploymentSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Employment
#         fields = '__all__'
#
#
# class OrgsHierarchyRelSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = OrgsHierarchyRel
#         fields = '__all__'
#
#
# class OrgsStructuralRelSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = OrgsStructuralRel
#         fields = '__all__'
#
#
# class SubordinateOrgsSerializer(serializers.ModelSerializer):
#     subordinate_org = OrgSerializer(many=False, read_only=True)
#
#     class Meta:
#         model = OrgsHierarchyRel
#         fields = chronoModelFields + ('subordinate_org', )
#
#
# class SuperiorOrgsSerializer(serializers.ModelSerializer):
#     superior_org = OrgSerializer(many=False, read_only=True)
#
#     class Meta:
#         model = OrgsHierarchyRel
#         fields = chronoModelFields + ('superior_org', )
#
#
# class ShortSuperiorOrgsSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = OrgsHierarchyRel
#         fields = chronoModelFields + ('superior_org', )
#
#
# class ExternalOrgsSerializer(serializers.ModelSerializer):
#     external_org = OrgSerializer(many=False, read_only=True)
#
#     class Meta:
#         model = OrgsStructuralRel
#         fields = chronoModelFields + ('external_org', )
#
#
# class PositionOrgHierarchyRelSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = PositionOrgHierarchyRel
#         fields = '__all__'
#
#
# class OrgPositionHierarchyRelSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = OrgPositionHierarchyRel
#         fields = '__all__'
#
# class PositionsHierarchyRelSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = PositionsHierarchyRel
#         fields = '__all__'
#
#
# class SuperiorPosToOrgSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = PositionOrgHierarchyRel
#         fields = chronoModelFields + ('superior_position', )
#
# class OrgConnectionsSerializer(serializers.ModelSerializer):
#     superior_orgs = ShortSuperiorOrgsSerializer(many=True, read_only=True)
#     superior_positions = SuperiorPosToOrgSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Org
#         fields = '__all__'
#
#
# class SuperiorPositionsSerializer(serializers.ModelSerializer):
#     superior_position = PositionSerializer(read_only=True)
#
#     class Meta:
#         model = PositionsHierarchyRel
#         fields = chronoModelFields + ('superior_position', )
#
# class SuperiorOrgToPosSerializer(serializers.ModelSerializer):
#     su
#
#     class Meta:
#         model = OrgPositionHierarchyRel
#         fields = chronoModelFields + ('superior_org', )
#
#
# class PositionConnectionsSerializer(serializers.ModelSerializer):
#     superior_positions = SuperiorPositionsSerializer(many=True, read_only=True)
#     superior_orgs = SuperiorOrgToPosSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Org
#         fields = '__all__'
#
#
# class InternalOrgsSerializer(serializers.ModelSerializer):
#     internal_org = OrgConnectionsSerializer(many=False, read_only=True)
#
#     class Meta:
#         model = OrgsStructuralRel
#         fields = chronoModelFields + ('internal_org',)
#
#
# class OrgProfileSerializer(serializers.ModelSerializer):
#     internal_orgs = OrgConnectionsSerializer(many=True, read_only=True)
#     external_orgs = ExternalOrgsSerializer(many=True, read_only=True)
#     subordinate_orgs = SubordinateOrgsSerializer(many=True, read_only=True)
#     superior_orgs = SuperiorOrgsSerializer(many=True, read_only=True)
#     positions = PositionSerializer(many=True, read_only=True)
#
#     class Meta:
#         model = Org
#         fields = '__all__'