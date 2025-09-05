from django.db import models
# Create your models here.

class Desha(models.Modle):
    title = models.CharField(max_lenght =200)
    author = models.CharField(max_lenght =100)
    published_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title