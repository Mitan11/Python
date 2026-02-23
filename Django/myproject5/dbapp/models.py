from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15 , default='0000000000')
    course = models.CharField(max_length=100 , default='Msc IT')
    totalMarks = models.IntegerField(default=0)
    percentage = models.CharField(max_length=100, default='0%')
    # to show roll and name in admin panel instead of object
    # def __str__(self):
    #     return f"{self.roll}  {self.name}"


class Marks(models.Model):
    studentRoll = models.ForeignKey(Student, on_delete=models.CASCADE)
    cn = models.IntegerField(default=0)
    dbms = models.IntegerField(default=0)
    python = models.IntegerField(default=0)
    aiml = models.IntegerField(default=0)

