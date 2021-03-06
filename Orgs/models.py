from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class ChronoModel(models.Model):
    description = models.TextField(name="description", blank=True, null=True)
    start_year = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(2050),
            MinValueValidator(1950)
        ]
    )
    start_month = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(12),
            MinValueValidator(1)
        ]
    )
    start_day = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(31),
            MinValueValidator(1)
        ]
    )
    end_year = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(2050),
            MinValueValidator(1950)
        ]
    )
    end_month = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(12),
            MinValueValidator(1)
        ]
    )
    end_day = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(31),
            MinValueValidator(1)
        ]
    )

    class Meta:
        abstract = True


class Org(ChronoModel):
    name = models.CharField(name="name", max_length=200)
    predecessor_orgs = models.ManyToManyField("self", blank=True, null=True)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    second_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200, blank=True, null=True)
    additional_info = models.TextField(blank=True, null=True)

    birth_year = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(2050),
            MinValueValidator(1800)
        ]
    )
    birth_month = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(12),
            MinValueValidator(1)
        ]
    )
    birth_day = models.IntegerField(
        blank=True,
        null=True,
        validators=[
            MaxValueValidator(31),
            MinValueValidator(1)
        ]
    )

    def __str__(self):
        return (self.second_name + " "
                + self.first_name + " "
                + self.middle_name)


class PositionName(models.Model):
    name = models.CharField(name="name", max_length=400)

    def __str__(self):
        return self.name


class Position(ChronoModel):
    name = models.ForeignKey(PositionName, on_delete=models.CASCADE)
    org = models.ForeignKey(Org,
                            on_delete=models.CASCADE,
                            related_name="positions")

    def __str__(self):
        return self.name.name + ", " + self.org.name


class Employment(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return (self.person + ", "
                + self.position + ", "
                + self.org)


class OrgsHierarchyRel(ChronoModel):
    superior_org = models.ForeignKey(Org,
                                     on_delete=models.CASCADE,
                                     related_name="subordinate_orgs")
    subordinate_org = models.ForeignKey(Org,
                                        on_delete=models.CASCADE,
                                        related_name="superior_orgs")

    def __str__(self):
        return self.superior_org + " supervises " + self.subordinate_org


class OrgsStructuralRel(ChronoModel):
    external_org = models.ForeignKey(Org,
                                     on_delete=models.CASCADE,
                                     related_name="internal_orgs")
    internal_org = models.ForeignKey(Org,
                                     on_delete=models.CASCADE,
                                     related_name="external_orgs")

    def __str__(self):
        return self.internal_org + " part of " + self.external_org


class PositionOrgHierarchyRel(ChronoModel):
    superior_position = models.ForeignKey(Position, on_delete=models.CASCADE)
    subordinate_org = models.ForeignKey(Org, on_delete=models.CASCADE)

    def __str__(self):
        return self.superior_position + " supervises " + self.subordinate_org


class PositionsHierarchyRel(ChronoModel):
    superior_position = models.ForeignKey(Position,
                                          on_delete=models.CASCADE,
                                          related_name="superior_position")
    subordinate_position = models.ForeignKey(Position,
                                             on_delete=models.CASCADE,
                                             related_name="subordinate_position")

    def __str__(self):
        return self.superior_position + \
               " supervises " + \
               self.subordinate_position


class OrgPositionHierarchyRel(ChronoModel):
    superior_org = models.ForeignKey(Org, on_delete=models.CASCADE)
    subordinate_position = models.ForeignKey(Position, on_delete=models.CASCADE)

    def __str__(self):
        return self.superior_org + " supervises " + self.subordinate_position


