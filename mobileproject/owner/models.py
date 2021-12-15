from datetime import date, timedelta

from django.db import models

# Create your models here.
class Mobile(models.Model):
    objects = None
    mobile_name=models.CharField(max_length=50,unique=True)
    company=models.TextField(max_length=50)
    price=models.PositiveIntegerField()
    stocks=models.PositiveIntegerField()
    image=models.ImageField(upload_to='images',null=True)

    def __str__(self):
        return self.mobile_name


class Order(models.Model):
    objects = None
    product = models.ForeignKey(Mobile, on_delete=models.CASCADE)
    user = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    options = (("ordered", "ordered"),
               ("delivered", "delivered"),
               ("cancelled", "cancelled"),
               ("in transist", "in transist"))
    status = models.CharField(max_length=20, choices=options, default="ordered")
    phone = models.CharField(max_length=10)
    edd=date.today()+timedelta(days=5)
    expected_delivery = models.DateField(null=True,default=edd)
