from django.db import models
from projects.models import Project  # Assuming you're linking to projects
from organizations.models import Organization  # If households are tied to specific organizations
from django.contrib.auth import get_user_model

class Household(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='households', null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='households', null=True, blank=True)
    head_of_household = models.CharField(max_length=255)
    number_of_members = models.PositiveIntegerField()
    address = models.TextField()
    location = models.CharField(max_length=255)  # Can represent a physical location or GPS
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Household in {self.location} led by {self.head_of_household}"


class HouseholdMember(models.Model):
    household = models.ForeignKey(Household, on_delete=models.CASCADE, related_name='members')
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=50)
    relationship_to_head = models.CharField(max_length=255)  # e.g., Spouse, Child, etc.
    
    def __str__(self):
        return f"{self.name} ({self.relationship_to_head})"

