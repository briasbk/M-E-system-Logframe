from django.contrib import admin
from .models import Household

@admin.register(Household)
class HouseholdAdmin(admin.ModelAdmin):
    list_display = ('head_of_household', 'number_of_members', 'location', 'project')
    list_filter = ('project', 'location')
    search_fields = ('head_of_household',)
