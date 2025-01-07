from django.contrib import admin
from .models import Project, Goal, Outcome, Output

class GoalInline(admin.TabularInline):
    model = Goal
    extra = 1


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'organization', 'created_at', 'updated_at')
    list_filter = ('organization', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    ordering = ('created_at',)
    inlines = [GoalInline]




@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'project')
    list_filter = ('project',)
    search_fields = ('description',)
    autocomplete_fields = ['project']  # Optimizes project selection for large datasets

@admin.register(Outcome)
class OutcomeAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'goal')
    list_filter = ('goal',)
    search_fields = ('description',)
    autocomplete_fields = ['goal']  # Optimizes goal selection for large datasets

@admin.register(Output)
class OutputAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'outcome')
    list_filter = ('outcome',)
    search_fields = ('description',)
    autocomplete_fields = ['outcome']  # Optimizes outcome selection for large datasets

