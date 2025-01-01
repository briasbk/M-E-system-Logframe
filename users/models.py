from django.contrib.auth.models import AbstractUser
from django.db import models

from organizations.models import Organization

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('evaluator', 'Evaluator'),
        ('stakeholder', 'Stakeholder'),
    ]
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="users", null=True, blank=True)

    def __str__(self):
        return f"{self.username} ({self.organization.name if self.organization else 'No Organization'})"

