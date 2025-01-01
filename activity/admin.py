from django.contrib import admin
from .models import Activity, Indicator, Assumption

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('id', 'output', 'description', 'start_date', 'end_date')
    list_filter = ('output', 'start_date', 'end_date')
    search_fields = ('description',)
    ordering = ('start_date',)

@admin.register(Indicator)
class IndicatorAdmin(admin.ModelAdmin):
    list_display = ('id', 'activity', 'name', 'target_value', 'achieved_value', 'means_of_verification')
    list_filter = ('activity',)
    search_fields = ('name', 'means_of_verification')
    ordering = ('name',)

@admin.register(Assumption)
class AssumptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'activity', 'description')
    list_filter = ('activity',)
    search_fields = ('description',)
