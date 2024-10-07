from django.db import models

# Create your models here.
class DestinationData(models.Model):
    place_name = models.CharField(max_length=500)
    picture = models.CharField(max_length=2500)
    description = models.CharField(max_length=1500)
    country = models.CharField(max_length=500)
    state = models.CharField(max_length=500)
    weather = models.CharField(max_length=500)
    activity = models.CharField(max_length=500)
    location = models.CharField(max_length=1500)

    def __str__(self):
        return self.place_name