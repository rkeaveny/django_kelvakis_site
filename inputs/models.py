from django.db import models
from django.utils import timezone

class Baser(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    description = models.TextField()
    added = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-added',)

    def __str__(self):
        return self.name
