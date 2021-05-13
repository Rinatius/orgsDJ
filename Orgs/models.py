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
    json_schema = models.JSONField(null=True, blank=True)
    ui_schema = models.JSONField(null=True, blank=True)
    REACT_JSONSCHEMA_FORM = "RJSF"
    JSONSCHEMA_LIBRARY_CHOICES = [
        (REACT_JSONSCHEMA_FORM, "React JSON Schema Form"),
    ]
    jsonschema_library = models.CharField(max_length=4,
                                          choices=JSONSCHEMA_LIBRARY_CHOICES,
                                          default=REACT_JSONSCHEMA_FORM)

    class Meta:
        abstract = True


class EdgeType(TypeModel):

    def __str__(self):
        return self.type


class NodeType(TypeModel):
    default_display_set = models.ForeignKey("DisplaySet",
                                            models.SET_NULL,
                                            blank=True,
                                            null=True,)

    def __str__(self):
        return self.type


class ValidEdgeCombination(models.Model):
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
        return (self.left_node.__str__() + "--" +
                self.edge_type.__str__() + "-->" +
                self.right_node.__str__())


class Node(ChronoModel):
    node_type = models.ForeignKey(NodeType, on_delete=models.CASCADE)
    short_name = models.CharField(max_length=200)
    aliases = models.TextField(blank=True)
    description = models.TextField(name="description", blank=True, null=True)
    json_data = models.JSONField(null=True)

    def __str__(self):
        return self.short_name


class Edge(ChronoModel):
    edge_type = models.ForeignKey(EdgeType, on_delete=models.CASCADE)
    left_node = models.ForeignKey(Node,
                                  on_delete=models.CASCADE,
                                  related_name="right_edges")
    right_node = models.ForeignKey(Node,
                                   on_delete=models.CASCADE,
                                   related_name="left_edges")


class Display(models.Model):
    name = models.CharField(max_length=200)
    parent_node_type = models.ForeignKey(NodeType, on_delete=models.CASCADE)
    valid_edge_combinations = models.ManyToManyField(ValidEdgeCombination)
    GRAPH = "GR"
    TREE = "TR"
    TEXT = "TX"
    LINK = "LI"
    CHRONOLOGY = "CH"
    AGGREGATION = "AG"
    DISPLAY_TYPE_CHOICES = [
        (GRAPH, "Graph"),
        (TREE,  "Tree"),
        (TEXT, "Text"),
        (LINK, "Link"),
        (CHRONOLOGY, "Chronology"),
        (AGGREGATION, "Aggregation")
    ]
    display_type = models.CharField(max_length=2,
                                    choices=DISPLAY_TYPE_CHOICES,
                                    default=GRAPH)

    def __str__(self):
        return self.name


class DisplaySet(models.Model):
    name = models.CharField(max_length=200)
    node_type = models.ForeignKey(NodeType,
                                  on_delete=models.CASCADE,
                                  related_name="display_sets")
    displays = models.ManyToManyField(Display, through="DisplayOrder")

    def __str__(self):
        return self.name


class DisplayOrder(models.Model):
    order = models.IntegerField()
    display = models.ForeignKey(Display, on_delete=models.CASCADE)
    display_set = models.ForeignKey(DisplaySet, on_delete=models.CASCADE)

    def __str__(self):
        return (str(self.order) + " " +
                self.display.__str__() + "@" +
                self.display_set.__str__())
