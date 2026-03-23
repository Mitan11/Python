from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=50)
    date_of_joining = models.DateField()

    # def __str__(self):
    #     return f"{self.name} , {self.department}"