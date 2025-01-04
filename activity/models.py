from django.db import models
from projects.models import Output

class Activity(models.Model):
    output = models.ForeignKey(Output, on_delete=models.CASCADE, related_name="activities")
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"Activity for Output: {self.output.id}"

class Indicator(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="indicators")
    name = models.CharField(max_length=255)
    target_value = models.FloatField()
    achieved_value = models.FloatField(default=0)
    means_of_verification = models.TextField()

    def __str__(self):
        return f"Indicator: {self.name}"

class Assumption(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="assumptions")
    description = models.TextField()

    def __str__(self):
        return f"Assumption for Activity: {self.activity.id}, {self.activity.description}"
    

