from django.db import models
from users.models import User

# Create your models here.
class Movie(models.Model):
    name = models.CharField(max_length=150)
    director = models.CharField(max_length=100)
    release_date = models.DateField()
    synopsis = models.TextField()
    watched = models.ManyToManyField(User, related_name='watched', blank=True)          # ManyToManyField to relate to users who have watched the movie

    def __str__(self):
        return self.name
