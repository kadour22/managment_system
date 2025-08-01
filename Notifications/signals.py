from django.db.models.signals import post_save
from django.dispatch import receiver
from Bug.models import Bug
from .models import Notification
from User.models import User

@receiver(post_save, sender=Bug)
def create_bug_notification(sender, instance, created, **kwargs) :
    # developer = User.objects.filter(role="Developer")
    if created :
        notification = Notification.objects.create(
            message  = "new bug founded..",
            recivers = instance.assigned_to 
        )
        notification.save()