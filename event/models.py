from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import Http404
from django.utils import timezone
from character.models import Character

import datetime


class Event(models.Model):
    name = models.CharField(max_length=30)
    character = models.ForeignKey(Character, related_name='event', default=None, on_delete=models.CASCADE)
    money = models.IntegerField(default=0)
    created_on = models.DateTimeField(default=timezone.now, blank=True)
    icon = models.CharField(max_length=30, default=None, null=True,blank=True)
    class Meta:
        ordering = ['-created_on',]


@receiver(post_save, sender=Event)
def handle_on_answer(sender, instance, created, **kwargs):
    if created == True:
        try:
            character = instance.character
            character.last_log = instance.created_on
            character.sum += instance.money
            character.save()
        except:
            raise Http404