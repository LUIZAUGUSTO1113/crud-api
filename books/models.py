from django.db import models
from users.models import User

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.TextField()
    publisher = models.TextField()
    publication_date = models.DateField()
    synopsis = models.TextField()
    pages_number = models.IntegerField()
    isbn_10 = models.CharField(max_length=10)
    isbn_13 = models.CharField(max_length=14)
    read = models.ManyToManyField(User, related_name='read', blank=True)            # ManyToManyField to relate to users who have read the book

    def __str__(self):
        return self.name
        