from django.db import models
from Project.models import Project
from User.models import User

class Bug(models.Model):
    STATUS_CHOICES = [
        ("Open", "Open"),
        ("In Progress", "In Progress"),
        ("Resolved", "Resolved"),
        ("Closed", "Closed"),
    ]

    PRIORITY_CHOICES = [
        ("Low", "Low"),
        ("Medium", "Medium"),
        ("High", "High"),
        ("Critical", "Critical"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="bugs")
    reported_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="reported_bugs")
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="assigned_bugs")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="Open")
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES, default="Medium")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title