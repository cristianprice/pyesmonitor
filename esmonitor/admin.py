from django.contrib import admin

# Register your models here.
from .models import ClusterHost, Stats


class ClusterHostAdmin(admin.ModelAdmin):
    pass


class StatsAdmin(admin.ModelAdmin):
    pass


admin.site.register(ClusterHost, ClusterHostAdmin)
admin.site.register(Stats, StatsAdmin)
