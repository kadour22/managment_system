from django.db import models
from User.models import User

class Notification(models.Model) :
    message    = models.CharField(max_length=255)
    recivers   = models.ForeignKey(User, on_delete=models.CASCADE ,related_name="notifications")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message