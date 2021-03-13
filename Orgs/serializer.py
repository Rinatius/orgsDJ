from rest_framework import serializers
from .models import Org, Person, Position, PositionName, Employment


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