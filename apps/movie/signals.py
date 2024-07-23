from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import *


@receiver(signal=post_save, sender=MovieModel)
def movie_notification(sender, instance, created, **kwargs):
    if created:
        comment = instance
        # AdminNotificationModel.objects.create(title=f'یک کامنت محصول از طرف کاربر{comment.user.fullname} ',
        #                                       type='product_comment', product_comment=comment)
        # channel_layer = get_channel_layer()
        # async_to_sync(channel_layer.group_send)(
        #     'comment_notification',
        #     {
        #         "type": "send_notification",
        #         "message": f'یک کامنت محصول از طرف کاربر{comment.user.fullname} '
        #     }
        # )