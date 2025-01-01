from django.db import models
from projects.models import Project
from activity.models import Activity

class Household(models.Model):
    activities = models.ManyToManyField(Activity, related_name="households")
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="households")
    head_of_household = models.CharField(max_length=255)  # Name of the head of the household
    number_of_members = models.PositiveIntegerField()
    location = models.CharField(max_length=255)  # General location description or GPS coordinates
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Household: {self.head_of_household} ({self.number_of_members} members)"
