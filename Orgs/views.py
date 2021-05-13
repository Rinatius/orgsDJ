from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from django.db.models import Q
from .models import EdgeType, Edge, Node, NodeType, ValidEdgeCombination
from .serializer import EdgeTypeSerializer, EdgeSerializer, \
    NodeSerializer, NodeTypeSerializer, ValidEdgeSerializer, LeftEdgeSerializer, RightEdgeSerializer
from drf_multiple_model.views import ObjectMultipleModelAPIView


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

    queryset = ValidEdgeCombination.objects.all()
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


class NodeRelsView(ObjectMultipleModelAPIView):

    def get_querylist(self):
        pk = self.request.query_params['pk']
        root_node = Node.objects.filter(pk=pk)
        left_edges = Edge.objects.filter(right_node_id=pk)
        right_edges = Edge.objects.filter(left_node_id=pk)
        left_nodes_ids = left_edges.values_list('left_node', flat=True)
        right_nodes_ids = right_edges.values_list('right_node', flat=True)
        n_nodes_ids = left_nodes_ids.union(right_nodes_ids)
        n_nodes_edges = Edge.objects.filter(left_node_id__in=n_nodes_ids) \
            .filter(right_node_id__in=n_nodes_ids)

        querylist = (
            {'queryset': root_node,
             'serializer_class': NodeSerializer,
             'label': 'root_node'},
            {'queryset': left_edges,
             'serializer_class': LeftEdgeSerializer,
             'label': 'left_edges'},
            {'queryset': right_edges,
             'serializer_class': RightEdgeSerializer,
             'label': 'right_edges'},
            {'queryset': n_nodes_edges,
             'serializer_class': EdgeSerializer,
             'label': 'n_nodes_edges'}
        )

        return querylist

    # def get(self, request, pk, format=None):
    #     # try:
    #     #     node = Node.objects.get(pk=pk).prefetch_related('left_edges',
    #     #                                                     'right_edges')
    #     #     #serializer = EdgeTypeSerializer(objects)
    #     #     return Response(node.json_data)
    #     # except:
    #     #     return Response(status=status.HTTP_404_NOT_FOUND)
    #
    #     #node = Node.objects.get(pk=pk)
    #     root_node = Node.objects.filter(pk=pk)
    #     # edges = Edge.objects.filter(Q(left_node_id=pk) | Q(right_node_id=pk))
    #     left_edges = Edge.objects.filter(right_node_id=pk)
    #     right_edges = Edge.objects.filter(left_node_id=pk)
    #     left_nodes_ids = left_edges.values_list('left_node', flat=True)
    #     right_nodes_ids = right_edges.values_list('right_node', flat=True)
    #     n_nodes_ids = left_nodes_ids.union(right_nodes_ids)
    #     n_nodes = Node.objects.filter(id__in=n_nodes_ids)
    #     n_nodes_edges = Edge.objects.filter(left_node_id__in=n_nodes_ids)\
    #                                 .filter(right_node_id__in=n_nodes_ids)
    #     # n_nodes_edges1 = Edge.objects.filter(left_node_id__in=n_nodes_ids)\
    #     #                              .exclude(right_node_id=pk)
    #     # n_nodes_edges2 = Edge.objects.filter(right_node_id__in=n_nodes_ids) \
    #     #     .exclude(left_node_id=pk)
    #     # intersect = n_nodes_edges1.intersection(n_nodes_edges2)
    #     # neighbor_nodes =
    #     # neighbor_nodes = Node.objects\
    #     #                      .filter(Q(left_edges__left_node_id=pk) |
    #     #                              Q(right_edges__right_node_id=pk))\
    #     #                      .distinct()
    #
    #     # print(qs.values())
    #     serializer = EdgeSerializer(n_nodes_edges, many=True)
    #     #qsl = list(qs)
    #     return Response(serializer.data)