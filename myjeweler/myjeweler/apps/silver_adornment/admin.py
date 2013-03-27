from django.contrib import admin
from myjeweler.apps.silver_adornment.models import SilverRings, TypeEarrings, SilverEarrings, TypePendants, Pendants


admin.site.register(SilverRings)
admin.site.register(SilverEarrings)
admin.site.register(TypePendants)
admin.site.register(TypeEarrings)
admin.site.register(Pendants)