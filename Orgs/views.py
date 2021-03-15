from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import Org, Person, Position, PositionName, \
    Employment, OrgsHierarchyRel, OrgsStructuralRel, PositionOrgHierarchyRel, OrgPositionHierarchyRel, \
    PositionsHierarchyRel
from .serializer import OrgSerializer, PersonSerializer, PositionSerializer, \
    PositionNameSerializer, EmploymentSerializer, OrgsHierarchyRelSerializer, OrgsStructuralRelSerializer, \
    PositionOrgHierarchyRelSerializer, OrgPositionHierarchyRelSerializer, PositionsHierarchyRelSerializer, \
    OrgProfileSerializer


# Create your views here.


class AllOrgs(ListAPIView):

    queryset = Org.objects.all()
    serializer_class = OrgSerializer

    def post(self, request, format=None):
        serializer = OrgSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrgView(APIView):

    def get(self, request, pk, format=None):
        try:
            org = Org.objects.get(pk=pk)
            serializer = OrgSerializer(org)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        org = Org.objects.get(pk=pk)
        org.delete()
        return Response(status=status.HTTP_200_OK)


class AllPersons(ListAPIView):

    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def post(self, request, format=None):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PersonView(APIView):

    def get(self, request, pk, format=None):
        try:
            person = Person.objects.get(pk=pk)
            serializer = PersonSerializer(person)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        org = Person.objects.get(pk=pk)
        org.delete()
        return Response(status=status.HTTP_200_OK)


class AllPositions(ListAPIView):

    queryset = Position.objects.all()
    serializer_class = PositionSerializer

    def post(self, request, format=None):
        serializer = PositionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PositionView(APIView):

    def get(self, request, pk, format=None):
        try:
            position = Position.objects.get(pk=pk)
            serializer = PositionSerializer(position)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        org = Position.objects.get(pk=pk)
        org.delete()
        return Response(status=status.HTTP_200_OK)


class AllPositionNames(ListAPIView):

    queryset = PositionName.objects.all()
    serializer_class = PositionNameSerializer

    def post(self, request, format=None):
        serializer = PositionNameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PositionNameView(APIView):

    def get(self, request, pk, format=None):
        try:
            position_name = PositionName.objects.get(pk=pk)
            serializer = PositionNameSerializer(position_name)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        org = PositionName.objects.get(pk=pk)
        org.delete()
        return Response(status=status.HTTP_200_OK)


class AllEmployments(ListAPIView):

    queryset = Employment.objects.all()
    serializer_class = EmploymentSerializer

    def post(self, request, format=None):
        serializer = EmploymentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmploymentView(APIView):

    def get(self, request, pk, format=None):
        try:
            employment = Employment.objects.get(pk=pk)
            serializer = EmploymentSerializer(employment)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        org = Employment.objects.get(pk=pk)
        org.delete()
        return Response(status=status.HTTP_200_OK)


class AllOrgsHierarchyRels(ListAPIView):

    queryset = OrgsHierarchyRel.objects.all()
    serializer_class = OrgsHierarchyRelSerializer

    def post(self, request, format=None):
        serializer = OrgsHierarchyRelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrgsHierarchyRelView(APIView):

    def get(self, request, pk, format=None):
        try:
            obj = OrgsHierarchyRel.objects.get(pk=pk)
            serializer = OrgsHierarchyRelSerializer(obj)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        obj = OrgsHierarchyRel.objects.get(pk=pk)
        obj.delete()
        return Response(status=status.HTTP_200_OK)


class AllOrgsStructuralRels(ListAPIView):

    queryset = OrgsStructuralRel.objects.all()
    serializer_class = OrgsStructuralRelSerializer

    def post(self, request, format=None):
        serializer = OrgsStructuralRelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrgsStructuralRelView(APIView):

    def get(self, request, pk, format=None):
        try:
            obj = OrgsStructuralRel.objects.get(pk=pk)
            serializer = OrgsStructuralRelSerializer(obj)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        obj = OrgsStructuralRel.objects.get(pk=pk)
        obj.delete()
        return Response(status=status.HTTP_200_OK)


class AllPositionOrgHierarchyRels(ListAPIView):

    queryset = PositionOrgHierarchyRel.objects.all()
    serializer_class = PositionOrgHierarchyRelSerializer

    def post(self, request, format=None):
        serializer = PositionOrgHierarchyRelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PositionOrgHierarchyRelView(APIView):

    def get(self, request, pk, format=None):
        try:
            obj = PositionOrgHierarchyRel.objects.get(pk=pk)
            serializer = PositionOrgHierarchyRelSerializer(obj)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        obj = PositionOrgHierarchyRel.objects.get(pk=pk)
        obj.delete()
        return Response(status=status.HTTP_200_OK)


class AllOrgPositionHierarchyRels(ListAPIView):

    queryset = OrgPositionHierarchyRel.objects.all()
    serializer_class = OrgPositionHierarchyRelSerializer

    def post(self, request, format=None):
        serializer = OrgPositionHierarchyRelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrgPositionHierarchyRelView(APIView):

    def get(self, request, pk, format=None):
        try:
            obj = OrgPositionHierarchyRel.objects.get(pk=pk)
            serializer = OrgPositionHierarchyRelSerializer(obj)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        obj = OrgPositionHierarchyRel.objects.get(pk=pk)
        obj.delete()
        return Response(status=status.HTTP_200_OK)


class AllPositionsHierarchyRels(ListAPIView):

    queryset = PositionsHierarchyRel.objects.all()
    serializer_class = PositionsHierarchyRelSerializer

    def post(self, request, format=None):
        serializer = PositionsHierarchyRelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PositionsHierarchyRelView(APIView):

    def get(self, request, pk, format=None):
        try:
            obj = PositionsHierarchyRel.objects.get(pk=pk)
            serializer = PositionsHierarchyRelSerializer(obj)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        obj = PositionsHierarchyRel.objects.get(pk=pk)
        obj.delete()
        return Response(status=status.HTTP_200_OK)

class AllOrgProfiles(ListAPIView):

    queryset = Org.objects.all()
    serializer_class = OrgProfileSerializer

