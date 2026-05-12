from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    rating = models.FloatField() 
    happy = models.IntegerField()
    action = models.IntegerField()
    weird = models.IntegerField()  

    def __str__(self):
        return f"{self.title} ({self.year})"