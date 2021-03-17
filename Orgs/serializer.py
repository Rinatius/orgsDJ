from rest_framework import serializers
from .models import Org, Person, Position, PositionName, Employment, OrgsHierarchyRel, OrgsStructuralRel, \
    PositionOrgHierarchyRel, OrgPositionHierarchyRel, PositionsHierarchyRel


class OrgSerializer(serializers.ModelSerializer):

    class Meta:
        model = Org
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Person
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Position
        fields = '__all__'


class PositionNameSerializer(serializers.ModelSerializer):

    class Meta:
        model = PositionName
        fields = '__all__'


class EmploymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employment
        fields = '__all__'


class OrgsHierarchyRelSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrgsHierarchyRel
        fields = '__all__'


class OrgsStructuralRelSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrgsStructuralRel
        fields = '__all__'


class SubordinateOrgsSerializer(serializers.ModelSerializer):
    subordinate_org = OrgSerializer(many=False, read_only=True)

    class Meta:
        model = OrgsHierarchyRel
        fields = ('subordinate_org', )


class SuperiorOrgsSerializer(serializers.ModelSerializer):
    superior_org = OrgSerializer(many=False, read_only=True)

    class Meta:
        model = OrgsHierarchyRel
        fields = ('superior_org', )


class InternalOrgsSerializer(serializers.ModelSerializer):
    internal_org = OrgSerializer(many=False, read_only=True)

    class Meta:
        model = OrgsStructuralRel
        fields = ('internal_org', )


class ExternalOrgsSerializer(serializers.ModelSerializer):
    external_org = OrgSerializer(many=False, read_only=True)

    class Meta:
        model = OrgsStructuralRel
        fields = ('external_org', )


class PositionOrgHierarchyRelSerializer(serializers.ModelSerializer):

    class Meta:
        model = PositionOrgHierarchyRel
        fields = '__all__'


class OrgPositionHierarchyRelSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrgPositionHierarchyRel
        fields = '__all__'

class PositionsHierarchyRelSerializer(serializers.ModelSerializer):

    class Meta:
        model = PositionsHierarchyRel
        fields = '__all__'


class OrgProfileSerializer(serializers.ModelSerializer):
    internal_orgs = InternalOrgsSerializer(many=True, read_only=True)
    external_orgs = ExternalOrgsSerializer(many=True, read_only=True)
    subordinate_orgs = SubordinateOrgsSerializer(many=True, read_only=True)
    superior_orgs = SuperiorOrgsSerializer(many=True, read_only=True)
    positions = PositionSerializer(many=True, read_only=True)

    class Meta:
        model = Org
        fields = '__all__'