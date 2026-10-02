from django.db import models
from django.contrib.auth.models import User
from tweet.models import Tweet

# Create your models here.
class Notification(models.Model):
    recipient= models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipient_notifications')
    actor= models.ForeignKey(User, on_delete=models.CASCADE, related_name='actor_notifications')
    tweet=models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='tweet_notifications',null=True, blank=True)
    notification_type=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    is_read=models.BooleanField(default=False)

    def __str__(self):
        return f'Notification for {self.recipient.username} from {self.actor.username} - {self.notification_type}'
