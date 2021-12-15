from django.db import models


# Create your models here.
class Work(models.Model):
    objects = None
    emp_name = models.CharField(max_length=100, unique=True)
    department = models.CharField(max_length=80)
    salary = models.PositiveIntegerField()
    experience = models.IntegerField()

    def __str__(self):
        return self.emp_name
