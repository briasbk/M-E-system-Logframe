from django.contrib import admin
from .models import Progress

# Register your models here.
@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('id', 'activity', 'date', 'update')
    list_filter = ('date', 'update')