from django.contrib import admin
from .models import Household, HouseholdMember

@admin.register(Household)
class HouseholdAdmin(admin.ModelAdmin):
    list_display = ('head_of_household', 'location', 'number_of_members')
    search_fields = ('head_of_household', 'location')

@admin.register(HouseholdMember)
class HouseholdMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'household', 'age', 'relationship_to_head')
    search_fields = ('name', 'household__head_of_household')
