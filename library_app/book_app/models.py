from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    pages = models.IntegerField()

    def __str__(self):
        return f"ID: {self.id} Title: {self.title}"