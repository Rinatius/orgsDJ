from rest_framework.relations import PrimaryKeyRelatedField
from rest_framework.schemas.openapi import AutoSchema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, filters, viewsets
from rest_framework.generics import ListAPIView
from django.db.models import Q
from .models import EdgeSchema, Edge, Node, NodeSchema, ValidEdge, Display, DisplaySet, DisplayOrder
from .serializer import EdgeTypeSerializer, EdgeSerializer, \
    NodeSerializer, NodeTypeSerializer, ValidEdgeTypeSerializer, LeftEdgeSerializer, RightEdgeSerializer, \
    WorkingNodeSerializer, LeftValidEdgeTypeSerializer, RightValidEdgeTypeSerializer, DisplaySerializer, \
    DisplaySetSerializer, DisplayOrderSerializer
from drf_multiple_model.views import ObjectMultipleModelAPIView


class BaseSchema(AutoSchema):
    """
    AutoSchema subclass that knows how to use extra_info.
    """
    # def get_responses(self, path, method):
    #     print(super().get_responses(path, method))
    #     response = super().get_responses(path, method)
    #     response_contents = response.get('200', False)
    #     if response_contents:
    #         response['200']['links'] = {
    #             'expandableSchema':
    #                 {'operationId': 'retrieveNodeSchema',
    #                                 'parameters':
    #                                     {'id': '$response.body#/schema'}}}
    #
    #     return response

    def get_responses(self, path, method):
        # print(super().get_responses(path, method))
        response = super().get_responses(path, method)
        response_contents = response.get('200', False)
        if response_contents:
            links = {}
            serializer = super().get_serializer(path, method)
            fields = serializer.get_fields()
            for field_name, field in fields.items():
                if isinstance(field, PrimaryKeyRelatedField):
                    expandable_field_name = 'expandable' + field_name.capitalize()
                    links[expandable_field_name] = {}
                    links[expandable_field_name]['operationId'] = 'retrieve' + field.queryset.model.__name__
                    links[expandable_field_name]['parameters'] = {'id': '$response.body#/' + field_name}
            if links:
                response['200']['links'] = links

            print(response)
            # response['200']['links']['expandableSchema'] = {'operationId': 'retrieveNodeSchema',
            #                                                 'parameters':
            #                                                     {'id': '$response.body#/schema'}}

        return response


    # def get_serializer(self, path, method):
    #     serializer = super().get_serializer(path, method)
    #     fields = serializer.get_fields()
    #     for key, field in fields.items():
    #         if isinstance(field, PrimaryKeyRelatedField):
    #             print(field.queryset)
    #             print(field.__class__)
    #             print(field.queryset.model)
    #             print(key)
    #             print(field)
    #             # try:
    #             #     print(field.queryset)
    #             #     print(field.__class__)
    #             #     print(field.queryset.model)
    #             #     print(key)
    #             #     print(field)
    #             # except:
    #             #     pass
    #     return serializer


# class CustomSchema(BaseSchema):
#     extra_info = "... some extra info .."

class EdgeTypeViewSet(viewsets.ModelViewSet):

    # schema = BaseSchema()
    serializer_class = EdgeTypeSerializer
    queryset = EdgeSchema.objects.all()


class ValidEdgeViewSet(viewsets.ModelViewSet):

    # schema = BaseSchema()
    serializer_class = ValidEdgeTypeSerializer
    queryset = ValidEdge.objects.all()


class EdgeViewSet(viewsets.ModelViewSet):

    # schema = BaseSchema()
    serializer_class = EdgeSerializer
    queryset = Edge.objects.all()


class NodeViewSet(viewsets.ModelViewSet):
    # schema = BaseSchema()
    serializer_class = NodeSerializer
    queryset = Node.objects.all()

    
class NodeValidEdges(ObjectMultipleModelAPIView):

    def get_querylist(self):
        pk = self.request.query_params['pk']
        root_node = Node.objects.filter(pk=pk)
        root_node_type = root_node.values_list('schema', flat=True)
        left_valid_edge_types = ValidEdge.objects \
            .filter(right_node_type__type__in=root_node_type)
        right_valid_edge_types = ValidEdge.objects\
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
    #     left_nodes_ids = left_edges.values_list('left_node_schema', flat=True)
    #     right_nodes_ids = right_edges.values_list('right_node_schema', flat=True)
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


class NodeTypeViewSet(viewsets.ModelViewSet):

    # schema = BaseSchema()
    serializer_class = NodeTypeSerializer
    queryset = NodeSchema.objects.all()


class DisplayViewSet(viewsets.ModelViewSet):

    # schema = BaseSchema()
    serializer_class = DisplaySerializer
    queryset = Display.objects.all()


class DisplaySetViewSet(viewsets.ModelViewSet):

    schema = BaseSchema()
    serializer_class = DisplaySetSerializer
    queryset = DisplaySet.objects.all()


class DisplayOrderViewSet(viewsets.ModelViewSet):

    # schema = BaseSchema()
    serializer_class = DisplayOrderSerializer
    queryset = DisplayOrder.objects.all()

