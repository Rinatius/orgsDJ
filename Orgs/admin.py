from django.contrib import admin
from .models import EdgeType, NodeType, ValidEdgeType, \
    Display, DisplaySet, DisplayOrder

admin.site.register(EdgeType)
admin.site.register(NodeType)
admin.site.register(ValidEdgeType)
admin.site.register(Display)
admin.site.register(DisplaySet)
admin.site.register(DisplayOrder)
