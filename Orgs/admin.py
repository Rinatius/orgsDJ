from django.contrib import admin
from .models import TipStructure, TieStructure, Display, DisplaySet, \
    DisplayOrder, Tip, Tie, Fact, TipFact, TieFact, TieQuestion, TipQuestion

admin.site.register(Tip)
admin.site.register(Tie)
admin.site.register(TipStructure)
admin.site.register(TieStructure)
admin.site.register(TipFact)
admin.site.register(TieFact)
admin.site.register(TipQuestion)
admin.site.register(TieQuestion)
admin.site.register(Display)
admin.site.register(DisplaySet)
admin.site.register(DisplayOrder)
