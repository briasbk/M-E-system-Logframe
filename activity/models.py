from django.db import models
from projects.models import Output
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from users.models import CustomUser

class Activity(models.Model):
    output = models.ForeignKey(Output, on_delete=models.CASCADE, related_name="activities")
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    # Progress and descriptions
    progress = models.IntegerField(default=0)  # Percentage or value
    current_progress_description = models.TextField()

    # Responsibilities - You can use User model or create a custom user model
    responsible_person = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)

    # Plan
    plan_start_date = models.DateField(null=True, blank=True)
    plan_end_date = models.DateField(null=True, blank=True)

    # Risks and Assumptions
    risks_and_assumptions = models.TextField(null=True, blank=True)

    # Need for action (Yes/No)
    need_for_action = models.BooleanField(default=False)

    # Location (Map coordinates can be stored as text or in a structured way)
    location = models.CharField(max_length=255, null=True, blank=True)

    # Notes
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Activity for Output: {self.output.id}"

# Task Model to represent tasks within the Activity
class Task(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="tasks")
    task_name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=50)  # E.g., 'Pending', 'In Progress', 'Completed'
    responsible_person = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True)
    progress = models.IntegerField(default=0)
    description = models.TextField()

    def __str__(self):
        return f"Task: {self.task_name} for Activity {self.activity.id}"


# Task Timeline Model to track task timelines
class TaskTimeline(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="timelines")
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Timeline for Task: {self.task.task_name}"

# Supporting Documents Model for activities
class SupportingDocument(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="supporting_documents")
    preview = models.ImageField(upload_to='documents/', null=True, blank=True)
    title = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    doc_type = models.CharField(max_length=50)  # Document type (e.g., PDF, Word, etc.)
    description = models.TextField()

    def __str__(self):
        return f"Document: {self.title} for Activity {self.activity.id}"

class Indicator(models.Model):
    # Indicator Type Choices
    INDICATOR_TYPE_CHOICES = [
        ('baseline', 'Baseline'),
        ('target', 'Target'),
        ('current', 'Current'),
        ('milestone', 'Milestone'),
    ]
    
    # These fields allow the indicator to connect with Goal, Outcome, Output, or Activity
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # Indicator Details
    name = models.CharField(max_length=255)
    indicator_type = models.CharField(
        max_length=10, choices=INDICATOR_TYPE_CHOICES, default='current'
    )
    target_value = models.FloatField()
    achieved_value = models.FloatField(default=0)
    means_of_verification = models.TextField()

    def __str__(self):
        return f"Indicator: {self.name} ({self.indicator_type}) for {self.content_object}"

    class Meta:
        verbose_name = "Indicator"
        verbose_name_plural = "Indicators"


class Assumption(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="assumptions")
    description = models.TextField()

    def __str__(self):
        return f"Assumption for Activity: {self.activity.id}, {self.activity.description}"
    

