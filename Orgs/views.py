from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.generics import ListAPIView
from .models import EdgeType, Edge, Node, NodeType, ValidEdge
from .serializer import EdgeTypeSerializer, EdgeSerializer, \
    NodeSerializer, NodeTypeSerializer, ValidEdgeSerializer


class AllEdgeTypes(ListAPIView):

    queryset = EdgeType.objects.all()
    serializer_class = EdgeTypeSerializer

    def post(self, request, format=None):
        serializer = EdgeTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EdgeTypeView(APIView):

    def get(self, request, pk, format=None):
        try:
            objects = EdgeType.objects.get(pk=pk)
            serializer = EdgeTypeSerializer(objects)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        obj = EdgeType.objects.get(pk=pk)
        obj.delete()
        return Response(status=status.HTTP_200_OK)


class AllValidEdges(ListAPIView):

    queryset = ValidEdge.objects.all()
    serializer_class = ValidEdgeSerializer

    def post(self, request, format=None):
        serializer = ValidEdgeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class AllNodeTypes(ListAPIView):

    queryset = NodeType.objects.all()
    serializer_class = NodeTypeSerializer

    def post(self, request, format=None):
        serializer = NodeTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AllNodes(ListAPIView):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer

    def post(self, request, format=None):
        serializer = NodeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class NodeSubClassFieldsMixin(object):
#
#     def get_queryset(self):
#         return Node.objects.select_subclasses()
#
#
# class RetrieveNodeAPIView(NodeSubClassFieldsMixin, generics.RetrieveDestroyAPIView):
#     serializer_class = NodeSerializer

