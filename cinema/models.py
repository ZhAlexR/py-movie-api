from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=63)
    description = models.TextField(blank=True)
    duration = models.DurationField(blank=True)
