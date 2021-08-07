from django.contrib import admin
from .models import TieStructure, TipStructure, TieStructure, \
    Display, DisplaySet, DisplayOrder

admin.site.register(TieStructure)
admin.site.register(TipStructure)
admin.site.register(Display)
admin.site.register(DisplaySet)
admin.site.register(DisplayOrder)
