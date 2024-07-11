from django.db import models
from django_jalali.db import models as jmodels
from apps.user.models import UserModel


class NotificationModel(models.Model):
    title = models.CharField(max_length=10000)
    image = models.ImageField(upload_to='notification/image', null=True, blank=True)
    user = models.ManyToManyField(UserModel, related_name='user_notifications')
    description = models.TextField(null=True, blank=True)
    date = jmodels.jDateTimeField(auto_now_add=True)
