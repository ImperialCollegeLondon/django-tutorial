from django.contrib import admin

# Register your models here.
from .models import Protein, Gene, StructureSegment, Organism

admin.site.register(Protein)
admin.site.register(Gene)
admin.site.register(StructureSegment)
admin.site.register(Organism)
