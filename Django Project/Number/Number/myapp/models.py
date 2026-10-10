from django.db import models

# Create your models here.

class number (models.Model):
    mark = models.IntegerField()
    time = models.IntegerField()

    def __str__(self):
        return self.mark