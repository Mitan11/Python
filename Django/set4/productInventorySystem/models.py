from django.db import models

# Create your models here.
class Inverntory(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.FloatField()
    category = models.CharField(max_length=100)
