from django.db import models
from datetime import timedelta,date

# Create your models here.
class Book(models.Model):
    objects = None
    book_name = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=80)
    price = models.PositiveIntegerField()
    copies = models.PositiveIntegerField()
    category = models.CharField(max_length=100,null=True)
    image = models.ImageField(upload_to="images",null=True)
    def __str__(self):
        return self.book_name


# book=Book(book_name='randamoozham',author='MT',price=230,copies=23)
# book.save()
# book=Book(book_name='Longnight',author='jk',price=6544,copies=456)
# book=Book(book_name='haming',author='ernest',price=900,copies=87)

# for all
# books=Book.objects.all()

# for book in books:
#    print(book.book_name,book.author,book.price,book.copies)

# orm for fetch a specific record
# reference=modelname.objects.get(feildname=value)
# book=Book.objects.get(id=1)


# orm for updating a specific record
# book=book.objects.get(id=1)
# book.price=349


# filter
# books=Book.objects.filter(price__lt=300) for lessthan 300
# books=Book.objects.filter(price__lte=300) for lessthanandequal
# books=Book.objects.filter(price__gt=300) for graeter
# books=Book.objects.filter(price__gte=300)

# category novel
# books=Book.objects.filter(category="novel")

class Order(models.Model):
    objects = None
    product = models.ForeignKey(Book, on_delete=models.CASCADE)
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
