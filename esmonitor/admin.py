from django.contrib import admin

# Register your models here.
from .models import ClusterHost, Stats, Settings


class ClusterHostAdmin(admin.ModelAdmin):
    pass


class StatsAdmin(admin.ModelAdmin):
    pass


class SettingsAdmin(admin.ModelAdmin):
    pass


admin.site.register(ClusterHost, ClusterHostAdmin)
admin.site.register(Stats, StatsAdmin)
admin.site.register(Settings, SettingsAdmin)
