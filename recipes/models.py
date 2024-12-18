from django.db import models

class Recipe(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    calories = models.IntegerField()
    suitable_for = models.CharField(max_length=50)
    region = models.CharField(max_length=50)

    def __str__(self):
        return self.name
