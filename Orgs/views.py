from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.generics import ListAPIView
from .models import Org, Person, Position, PositionType, EdgeType, Edge, Node
from .serializer import OrgSerializer, PersonSerializer, PositionSerializer, EdgeTypeSerializer, EdgeSerializer, \
    PositionTypeSerializer, NodeSerializer


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

    queryset = PositionType.objects.all()
    serializer_class = PositionTypeSerializer

    def post(self, request, format=None):
        serializer = PositionTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PositionNameView(APIView):

    def get(self, request, pk, format=None):
        try:
            position_name = PositionType.objects.get(pk=pk)
            serializer = PositionTypeSerializer(position_name)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        org = PositionType.objects.get(pk=pk)
        org.delete()
        return Response(status=status.HTTP_200_OK)


class AllEdgeNames(ListAPIView):

    queryset = EdgeType.objects.all()
    serializer_class = EdgeTypeSerializer

    def post(self, request, format=None):
        serializer = EdgeTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EdgeNameView(APIView):

    def get(self, request, pk, format=None):
        try:
            edge_name = EdgeType.objects.get(pk=pk)
            serializer = EdgeTypeSerializer(edge_name)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        edge_name = EdgeType.objects.get(pk=pk)
        edge_name.delete()
        return Response(status=status.HTTP_200_OK)


class AllEdges(ListAPIView):

    queryset = Edge.objects.all()
    serializer_class = EdgeSerializer

    def post(self, request, format=None):
        serializer = EdgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EdgeView(APIView):

    def get(self, request, pk, format=None):
        try:
            edge = Edge.objects.get(pk=pk)
            serializer = EdgeSerializer(edge)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        edge = Edge.objects.get(pk=pk)
        edge.delete()
        return Response(status=status.HTTP_200_OK)


class NodeSubClassFieldsMixin(object):

    def get_queryset(self):
        return Node.objects.select_subclasses()


class RetrieveNodeAPIView(NodeSubClassFieldsMixin, generics.RetrieveDestroyAPIView):
    serializer_class = NodeSerializer

