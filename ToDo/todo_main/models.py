import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Todo(models.Model):
    text = models.CharField(max_length=50)
    complete = models.BooleanField(default=False)
    date_added = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def recent_todo(self):
        now = timezone.now()
        return now - datetime.timedelta(hours=1) <= self.date_added <= now

    def __str__(self):
        return self.text
