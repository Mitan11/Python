from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(max_length=3)
    email = models.EmailField()
    date_of_join = models.DateField()