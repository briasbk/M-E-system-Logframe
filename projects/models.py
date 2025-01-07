from django.db import models
from organizations.models import Organization
from django.contrib.auth.models import User
# from users.models import CustomUser

class SDG(models.Model):
    # Define the SDG model with the name and a description.
    number = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=255)
    impact_sgds = models.TextField()

    class Meta:
        verbose_name = "Sustainable Development Goal"
        verbose_name_plural = "Sustainable Development Goals"

    def __str__(self):
        return f"SDG {self.number}: {self.title}"



class Project(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="projects")
    name = models.CharField(max_length=255)
    project_objective = models.TextField(null=True, blank=True)
    description = models.TextField()
    notes_summary = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    project_image = models.ImageField(upload_to='images/', null=True, blank=True)
    impact_sdgs = models.ManyToManyField(SDG, blank=True, symmetrical=False) 

    class Meta:
            verbose_name = "Project"
            verbose_name_plural = "Projects"

    def __str__(self):
        return self.name


class Project_Key_Data(models.Model):
    STATUS_CHOICES = [
        ('P', 'Pending'),
        ('C', 'Completed'),
        ('I', 'In Progress'),
    ]

    CURRENCY_CHOICES = [
        ('KES', 'Kenya Shillings'),
        ('UGX', 'Uganda Shillings'),
        ('USD', 'US Dollars'),
    ]

    # NEED_CHOICES = [
    #     ('N', 'No'),
    #     ('Y', 'Yes'),
    #     ('U', 'Unsure'),
    # ]
    project=models.ForeignKey(Project, on_delete=models.CASCADE, related_name="project_key_data")
    short_name = models.CharField(max_length=255)
    status = models.CharField(max_length=1,choices=STATUS_CHOICES,default='P')
    start_date = models.DateField()
    end_date = models.DateField()
    project_number = models.CharField(max_length=255)
    team_leader = models.CharField(max_length=255)
    project_locations = models.TextField()
    donor = models.CharField(max_length=100)
    budget = models.BigIntegerField()
    currency = models.CharField(max_length=100,choices=CURRENCY_CHOICES,default='USD')
    implementing_partners = models.TextField()
    beneficiaries = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Project Key Data"
        verbose_name_plural = "Project Key Data"

    def __str__(self):
        return self.short_name


# class Responsibilities(models.Model):
#     project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="responsibility")
    
#     # These will now reference the CustomUser model
#     finance = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, related_name='finance_responsibilities', null=True, blank=True)
#     communication = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='communication_responsibilities')
#     monitoring_evaluation = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='monitoring_responsibilities')

#     def __str__(self):
#         return f"Responsibilities for {self.project.name}"

    
class Progress(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="progress")
    progress = models.IntegerField(default=0)
    current_progress_description = models.TextField()
    challenges_or_opportunities = models.TextField()  # Use TextField for descriptive content
    # need_for_action = models.CharField(max_length=1, choices=NEED_CHOICES, default='N') # type: ignore
    action_to_be_taken = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Project Progress"
        verbose_name_plural = "Project Progress"

    def __str__(self):
        return f"Progress for {self.project.name}"  # Use the project's name


class Internet_Resources(models.Model):
    url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="link")
    
    class Meta:
            verbose_name = "Internet Resource"
            verbose_name_plural = "Internet Resources"

    def __str__(self):
        return self.url


class Goal(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="goals")
    description = models.TextField()

    class Meta:
        verbose_name = "Goal"
        verbose_name_plural = "Goals"

    def __str__(self):
        return f"Goal for {self.project.name}"


class Outcome(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, related_name="outcomes")
    description = models.TextField()

    class Meta:
        verbose_name = "Outcome"
        verbose_name_plural = "Outcomes"

    def __str__(self):
        return f"Outcome for Goal: {self.goal.id}"


class Output(models.Model):
    outcome = models.ForeignKey(Outcome, on_delete=models.CASCADE, related_name="outputs")
    description = models.TextField()

    class Meta:
        verbose_name = "Output"
        verbose_name_plural = "Outputs"

    def __str__(self):
        return f"Output for Outcome: {self.outcome.id}"