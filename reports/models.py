from django.db import models
from activity.models import Activity

class Progress(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="progress_updates")
    date = models.DateField()
    update = models.TextField()

    def __str__(self):
        return f"Progress for Activity: {self.activity.id} on {self.date}"
