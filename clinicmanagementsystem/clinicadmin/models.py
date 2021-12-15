from django.db import models
from datetime import date, timedelta


# Create your models here.
class Doctor(models.Model):
    objects = None
    doctor_name = models.CharField(max_length=100, unique=True)
    department = models.CharField(max_length=100)
    doctor_time = models.PositiveIntegerField()
    doctor_fee = models.PositiveIntegerField()



    def __str__(self):
        return self.doctor_name


class Appointment(models.Model):
    patient_name = models.CharField(max_length=100,unique=True,null=True)
    address = models.CharField(max_length=100,null=True)
    phone = models.CharField(max_length=10)
    date = models.DateField()
    options =("male","male"),("Female","Female")


    gender= models.CharField(max_length=10,choices=options,default="male")