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