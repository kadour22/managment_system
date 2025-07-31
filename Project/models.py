from django.db import models
from User.models import User

class Project(models.Model) :
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='project')
    members    = models.ManyToManyField(User, related_name='members')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name