import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class CurrentTask(models.Model):

    task = models.CharField(max_length=255)
    ONCE = 'One Time'
    WEEKLY = 'Weekly'
    MONTHLY = 'Monthly'
    FREQUENCY_CHOICES = ((ONCE, 'One Time'), (WEEKLY, 'Weekly'), (MONTHLY, 'Monthly'))
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES, default=ONCE)

    pub_date = models.DateTimeField('date published')
    date_due = models.DateTimeField('date due')
    #person_in_charge = models.ForeignKey(User)
    email = models.EmailField(max_length=254)

    def __unicode__(self):
        return self.task

    # to do:

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class TaskType(models.Model):
    #type = models.ForeignKey(CurrentTask)
    description = models.CharField(max_length=600)

    def __unicode__(self):
        return self.description