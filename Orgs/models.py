from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from model_utils.managers import InheritanceManager

# Create your models here.


class ChronoModel(models.Model):
    start_date = models.DateField(null=True)
    start_year_unknown = models.BooleanField(null=True, default=False)
    start_month_unknown = models.BooleanField(null=True, default=False)
    start_day_unknown = models.BooleanField(null=True, default=False)

    end_date = models.DateField(null=True)
    current = models.BooleanField(null=True, default=False)
    end_year_unknown = models.BooleanField(null=True, default=False)
    end_month_unknown = models.BooleanField(null=True, default=False)
    end_day_unknown = models.BooleanField(null=True, default=False)

    class Meta:
        abstract = True


class TypeModel(models.Model):
    type = models.CharField(max_length=100)
    additional_schema = models.JSONField(null=True)

    class Meta:
        abstract = True


class EdgeType(TypeModel):

    def __str__(self):
        return self.type


class NodeType(TypeModel):

    def __str__(self):
        return self.type


class ValidEdge(models.Model):
    edge_type = models.ForeignKey(EdgeType,
                                  on_delete=models.CASCADE,
                                  related_name="compatible_node_combos")
    left_node = models.ForeignKey(NodeType,
                                  on_delete=models.CASCADE,
                                  related_name="compatible_edges_right_nodes")
    right_node = models.ForeignKey(NodeType,
                                   on_delete=models.CASCADE,
                                   related_name="compatible_edges_left_nodes")

    def __str__(self):
        return (self.edge_type + ": "
                + self.left_node + " -> "
                + self.right_node)


class Node(ChronoModel):
    node_type = models.ForeignKey(NodeType, on_delete=models.CASCADE)
    short_name = models.CharField(max_length=200)
    aliases = models.TextField(blank=True)
    description = models.TextField(name="description", blank=True, null=True)
    json_data = models.JSONField(null=True)

    def __str__(self):
        return str(self.short_name)


class Edge(ChronoModel):
    edge_type = models.ForeignKey(EdgeType, on_delete=models.CASCADE)
    left_node = models.ForeignKey(Node,
                                  on_delete=models.CASCADE,
                                  related_name="right_edges")
    right_node = models.ForeignKey(Node,
                                   on_delete=models.CASCADE,
                                   related_name="left_edges")