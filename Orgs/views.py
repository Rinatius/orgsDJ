from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters, viewsets
from rest_framework.generics import ListAPIView
from django.db.models import Q
from .models import TieStructure, Tie, Tip, TipStructure, TieStructure, Display, DisplayCollection, DisplayOrder
from .serializer import EdgeTypeSerializer, EdgeSerializer, \
    NodeSerializer, NodeTypeSerializer, ValidEdgeTypeSerializer, LeftEdgeSerializer, RightEdgeSerializer, \
    WorkingNodeSerializer, LeftValidEdgeTypeSerializer, RightValidEdgeTypeSerializer, DisplaySerializer, \
    DisplaySetSerializer, DisplayOrderSerializer
from drf_multiple_model.views import ObjectMultipleModelAPIView


class EdgeTypeViewSet(viewsets.ModelViewSet):

    serializer_class = EdgeTypeSerializer
    queryset = TieStructure.objects.all()


class ValidEdgeViewSet(viewsets.ModelViewSet):

    serializer_class = ValidEdgeTypeSerializer
    queryset = TieStructure.objects.all()


class EdgeViewSet(viewsets.ModelViewSet):

    serializer_class = EdgeSerializer
    queryset = Tie.objects.all()


class NodeViewSet(viewsets.ModelViewSet):

    serializer_class = NodeSerializer
    queryset = Tip.objects.all()

    
class NodeValidEdges(ObjectMultipleModelAPIView):

    def get_querylist(self):
        pk = self.request.query_params['pk']
        root_node = Tip.objects.filter(pk=pk)
        root_node_type = root_node.values_list('structure', flat=True)
        left_valid_edge_types = TieStructure.objects \
            .filter(right_node_type__type__in=root_node_type)
        right_valid_edge_types = TieStructure.objects\
            .filter(left_node_type__type__in=root_node_type)

        querylist = (
            {'queryset': root_node,
             'serializer_class': WorkingNodeSerializer,
             'label': 'root_node'},
            {'queryset': left_valid_edge_types,
             'serializer_class': LeftValidEdgeTypeSerializer,
             'label': 'left_valid_edge_types'},
            {'queryset': right_valid_edge_types,
             'serializer_class': RightValidEdgeTypeSerializer,
             'label': 'right_valid_edge_types'},
        )

        return querylist


class NodeRelsView(ObjectMultipleModelAPIView):

    def get_querylist(self):
        pk = self.request.query_params['pk']
        root_node = Tip.objects.filter(pk=pk)
        left_edges = Tie.objects.filter(right_node_id=pk)
        right_edges = Tie.objects.filter(left_node_id=pk)
        left_nodes_ids = left_edges.values_list('left_tip', flat=True)
        right_nodes_ids = right_edges.values_list('right_tip', flat=True)
        n_nodes_ids = left_nodes_ids.union(right_nodes_ids)
        n_nodes_edges = Tie.objects.filter(left_node_id__in=n_nodes_ids) \
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
    #     #     node = Tip.objects.get(pk=pk).prefetch_related('left_edges',
    #     #                                                     'right_edges')
    #     #     #serializer = EdgeTypeSerializer(objects)
    #     #     return Response(node.json_data)
    #     # except:
    #     #     return Response(status=status.HTTP_404_NOT_FOUND)
    #
    #     #node = Tip.objects.get(pk=pk)
    #     root_node = Tip.objects.filter(pk=pk)
    #     # edges = Tie.objects.filter(Q(left_node_id=pk) | Q(right_node_id=pk))
    #     left_edges = Tie.objects.filter(right_node_id=pk)
    #     right_edges = Tie.objects.filter(left_node_id=pk)
    #     left_nodes_ids = left_edges.values_list('left_tip_structure', flat=True)
    #     right_nodes_ids = right_edges.values_list('right_tip_structure', flat=True)
    #     n_nodes_ids = left_nodes_ids.union(right_nodes_ids)
    #     n_nodes = Tip.objects.filter(id__in=n_nodes_ids)
    #     n_nodes_edges = Tie.objects.filter(left_node_id__in=n_nodes_ids)\
    #                                 .filter(right_node_id__in=n_nodes_ids)
    #     # n_nodes_edges1 = Tie.objects.filter(left_node_id__in=n_nodes_ids)\
    #     #                              .exclude(right_node_id=pk)
    #     # n_nodes_edges2 = Tie.objects.filter(right_node_id__in=n_nodes_ids) \
    #     #     .exclude(left_node_id=pk)
    #     # intersect = n_nodes_edges1.intersection(n_nodes_edges2)
    #     # neighbor_nodes =
    #     # neighbor_nodes = Tip.objects\
    #     #                      .filter(Q(left_edges__left_node_id=pk) |
    #     #                              Q(right_edges__right_node_id=pk))\
    #     #                      .distinct()
    #
    #     # print(qs.values())
    #     serializer = EdgeSerializer(n_nodes_edges, many=True)
    #     #qsl = list(qs)
    #     return Response(serializer.data)


class NodeTypeViewSet(viewsets.ModelViewSet):
    serializer_class = NodeTypeSerializer
    queryset = TipStructure.objects.all()


class DisplayViewSet(viewsets.ModelViewSet):
    serializer_class = DisplaySerializer
    queryset = Display.objects.all()


class DisplaySetViewSet(viewsets.ModelViewSet):
    serializer_class = DisplaySetSerializer
    queryset = DisplayCollection.objects.all()


class DisplayOrderViewSet(viewsets.ModelViewSet):
    serializer_class = DisplayOrderSerializer
    queryset = DisplayOrder.objects.all()
