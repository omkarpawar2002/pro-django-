from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.IntegerField()
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    marks = models.FloatField()
    city = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    mail = models.EmailField(max_length=200)
    address = models.TextField(max_length=200)
    dob = models.DateField()
    password = models.CharField(max_length=100)