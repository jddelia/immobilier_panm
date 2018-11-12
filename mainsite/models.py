from django.db import models
from django.utils import timezone

class Post(models.Model):
    location = models.CharField(max_length=200)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    image = models.TextField()
    more_photos = models.TextField(blank=True)
    price = models.CharField(max_length=75)
    alt = models.CharField(max_length=100)
    tags = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.location
