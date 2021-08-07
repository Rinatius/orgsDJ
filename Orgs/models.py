from django.db import models

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


class SourceRequirementModel(models.Model):
    sources_needed = models.BooleanField(default=False)

    class Meta:
        abstract = True


# class SchemaModel(models.Model):
#     name = models.CharField(max_length=100)
#     json_schema = models.JSONField(null=True, blank=True, help_text="Form JSON Schema.")
#     ui_schema = models.JSONField(null=True, blank=True)
#     REACT_JSONSCHEMA_FORM = "RJSF"
#     JSONSCHEMA_LIBRARY_CHOICES = [
#         (REACT_JSONSCHEMA_FORM, "React JSON Schema Form"),
#     ]
#     jsonschema_library = models.CharField(max_length=4,
#                                           choices=JSONSCHEMA_LIBRARY_CHOICES,
#                                           default=REACT_JSONSCHEMA_FORM)
#
#     class Meta:
#         abstract = True


class FactQuestion(SourceRequirementModel):
    name = models.CharField(max_length=200)
    display_name = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)
    TEXT_FORMAT = "TEXT"
    INT_FORMAT = "INT"
    FLOAT_FORMAT = "FLOAT"
    DATE_FORMAT = "DATE"
    FORMAT_CHOICES = [
        (TEXT_FORMAT, "TEXT"),
        (INT_FORMAT, "INT"),
        (FLOAT_FORMAT, "FLOAT"),
        (DATE_FORMAT, "DATE"),
    ]
    input_format = models.CharField(max_length=5,
                                    choices=FORMAT_CHOICES,
                                    default=TEXT_FORMAT)

    def __str__(self):
        return self.name


class FactQuestionSet(models.Model):
    name = models.CharField(max_length=200)
    fact_questions = models.ManyToManyField(FactQuestion,
                                            through="FactQuestionOrder")

    def __str__(self):
        return self.name


class FactQuestionOrder(models.Model):
    order = models.IntegerField()
    fact_question = models.ForeignKey(FactQuestion, on_delete=models.CASCADE)
    fact_question_set = models.ForeignKey(FactQuestionSet,
                                          on_delete=models.CASCADE)

    class Meta:
        unique_together = ["fact_question", "fact_question_set"]

    def __str__(self):
        return (str(self.order) + " " +
                self.fact_question.__str__() + "@" +
                self.fact_question_set.__str__())


class Fact(models.Model):
    response_text = models.TextField(blank=True, null=True)
    response_int = models.IntegerField(blank=True, null=True)
    response_float = models.FloatField(blank=True, null=True)
    response_date = models.DateField(blank=True, null=True)

    fact_question = models.ForeignKey(FactQuestion, on_delete=models.CASCADE)
    sources = models.ManyToManyField("Node", blank=True, null=True)

    def __str__(self):
        return (self.fact_question.__str__() + " : " +
                self.fact_question_set.__str__())


class NodeSchema(models.Model):
    name = models.CharField(max_length=200)
    fact_question_set = models.ForeignKey(FactQuestionSet,
                                          on_delete=models.CASCADE,
                                          blank=True,
                                          null=True)
    default_display_set = models.ForeignKey("DisplaySet",
                                            on_delete=models.SET_NULL,
                                            blank=True,
                                            null=True)

    def __str__(self):
        return self.name


class EdgeSchema(models.Model):
    fact_question_set = models.ForeignKey(FactQuestionSet,
                                    on_delete=models.CASCADE,
                                    related_name="edges")
    left_node_schema = models.ForeignKey(NodeSchema,
                                         on_delete=models.CASCADE,
                                         related_name="right_valid_edges")
    right_node_schema = models.ForeignKey(NodeSchema,
                                          on_delete=models.CASCADE,
                                          related_name="left_valid_edges")

    def __str__(self):
        return (self.left_node_schema.__str__() + "--" +
                self.edge_schema.__str__() + "-->" +
                self.right_node_schema.__str__())


class Node(ChronoModel):
    name = models.CharField(max_length=200, blank=True)
    description = models.TextField(name="description", blank=True)
    image = models.ImageField(name="image", null=True, blank=True)
    schema = models.ForeignKey(NodeSchema, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Edge(ChronoModel):
    edge_schema = models.ForeignKey(EdgeSchema, on_delete=models.CASCADE)
    left_node = models.ForeignKey(Node,
                                  on_delete=models.CASCADE,
                                  related_name="right_edges")
    right_node = models.ForeignKey(Node,
                                   on_delete=models.CASCADE,
                                   related_name="left_edges")


class Display(models.Model):
    name = models.CharField(max_length=200)
    parent_node_schema = models.ForeignKey(NodeSchema, on_delete=models.CASCADE)
    parent_left_valid_edges = models.ManyToManyField(EdgeSchema,
                                                     related_name="displays_right")
    parent_right_valid_edges = models.ManyToManyField(EdgeSchema,
                                                      related_name="displays_left")
    second_level_display = models.ManyToManyField("self",
                                                  symmetrical=False)
    GRAPH = "GR"
    TREE = "TR"
    TEXT = "TX"
    LINK = "LI"
    CHRONOLOGY = "CH"
    AGGREGATION = "AG"
    LENS_CHOICES = [
        (GRAPH, "Graph"),
        (TREE,  "Tree"),
        (TEXT, "Text"),
        (LINK, "Link"),
        (CHRONOLOGY, "Chronology"),
        (AGGREGATION, "Aggregation")
    ]
    lens = models.CharField(max_length=2,
                            choices=LENS_CHOICES,
                            default=GRAPH)

    def __str__(self):
        return self.name


class DisplaySet(models.Model):
    name = models.CharField(max_length=200)
    node_schema = models.ForeignKey(NodeSchema,
                                    on_delete=models.CASCADE,
                                    related_name="display_sets")
    displays = models.ManyToManyField(Display, through="DisplayOrder")

    def __str__(self):
        return self.name


class DisplayOrder(models.Model):
    order = models.IntegerField()
    display = models.ForeignKey(Display, on_delete=models.CASCADE)
    display_set = models.ForeignKey(DisplaySet, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["display", "display_set"]

    def __str__(self):
        return (str(self.order) + " " +
                self.display.__str__() + "@" +
                self.display_set.__str__())