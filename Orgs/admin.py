from django.contrib import admin
from .models import EdgeSchema, NodeSchema, EdgeSchema, \
    Display, DisplaySet, DisplayOrder

admin.site.register(EdgeSchema)
admin.site.register(NodeSchema)
admin.site.register(EdgeSchema)
admin.site.register(Display)
admin.site.register(DisplaySet)
admin.site.register(DisplayOrder)
