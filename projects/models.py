from django.db import models
from organizations.models import Organization

class Project(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="projects")
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Goal(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="goals")
    description = models.TextField()

    def __str__(self):
        return f"Goal for {self.project.name}"

class Outcome(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name="outcomes")
    description = models.TextField()

    def __str__(self):
        return f"Outcome for Goal: {self.goal.id}"

class Output(models.Model):
    outcome = models.ForeignKey(Outcome, on_delete=models.CASCADE, related_name="outputs")
    description = models.TextField()

    def __str__(self):
        return f"Output for Outcome: {self.outcome.id}"
