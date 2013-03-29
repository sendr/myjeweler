from django.contrib import admin
from myjeweler.apps.silver_adornment.models import SilverRings, TypeEarrings, SilverEarrings, TypePendants, Pendants



# class SilverRingInline(admin.StackedInline):
# 	model = SilverRings.name()
	# extra = 0


class SilverRingsAdmin(admin.ModelAdmin):
	list_display = ("name", "art", "weigth", "sex", "image")
	# inlines = True


class SilverEarringsAdmin(admin.ModelAdmin):
	list_display = ("name", "art", "weigth","type_earrings", "image")


class PendantsAdmin(admin.ModelAdmin):
	list_display = ("name", "art", "weigth","type_pendants", "image")


admin.site.register(SilverRings, SilverRingsAdmin)
admin.site.register(SilverEarrings, SilverEarringsAdmin)
admin.site.register(TypePendants)
admin.site.register(TypeEarrings)
admin.site.register(Pendants, PendantsAdmin)