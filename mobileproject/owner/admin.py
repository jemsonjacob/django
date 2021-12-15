from django.contrib import admin

# Register your models here.
from owner.models import Order,Mobile

admin.site.register(Order)
admin.site.register(Mobile)