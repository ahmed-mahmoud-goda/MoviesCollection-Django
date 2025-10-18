from django.db import models

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=80)
    category = models.CharField(max_length=50)
    released = models.DateField()
    description = models.TextField()
    image = models.URLField()
