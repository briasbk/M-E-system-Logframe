from django.contrib import admin
from .models import SDG, Project, Project_Key_Data, Progress, Internet_Resources, Goal, Outcome, Output

@admin.register(SDG)
class SDGAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'impact_sgds')
    search_fields = ('title', 'impact_sgds')
    list_filter = ('number',)

    # Adding verbose names for better display in admin
    def get_verbose_name(self, obj):
        return f"SDG {obj.number}: {obj.title}"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    list_filter = ('organization', 'created_at')
    # prepopulated_fields = {"slug": ("name",)}

    def get_verbose_name(self, obj):
        return f"Project: {obj.name}"


@admin.register(Project_Key_Data)
class ProjectKeyDataAdmin(admin.ModelAdmin):
    list_display = ('short_name', 'status', 'start_date', 'end_date', 'budget')
    search_fields = ('short_name', 'project_number', 'donor', 'implementing_partners')
    list_filter = ('status', 'currency')

    def get_verbose_name(self, obj):
        return f"Key Data for {obj.short_name}"


@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('project', 'progress', 'current_progress_description', 'challenges_or_opportunities')
    search_fields = ('project__name', 'current_progress_description')
    list_filter = ('project',)

    def get_verbose_name(self, obj):
        return f"Progress for {obj.project.name}"


@admin.register(Internet_Resources)
class InternetResourcesAdmin(admin.ModelAdmin):
    list_display = ('url', 'description', 'project')
    search_fields = ('url', 'description', 'project__name')
    list_filter = ('project',)

    def get_verbose_name(self, obj):
        return f"Resource Link: {obj.url}"


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('project', 'description')
    search_fields = ('project__name', 'description')
    list_filter = ('project',)

    def get_verbose_name(self, obj):
        return f"Goal for {obj.project.name}"


@admin.register(Outcome)
class OutcomeAdmin(admin.ModelAdmin):
    list_display = ('goal', 'description')
    search_fields = ('goal__project__name', 'description')
    list_filter = ('goal',)

    def get_verbose_name(self, obj):
        return f"Outcome for Goal: {obj.goal.id}"


@admin.register(Output)
class OutputAdmin(admin.ModelAdmin):
    list_display = ('outcome', 'description')
    search_fields = ('outcome__goal__project__name', 'description')
    list_filter = ('outcome',)

    def get_verbose_name(self, obj):
        return f"Output for Outcome: {obj.outcome.id}"
