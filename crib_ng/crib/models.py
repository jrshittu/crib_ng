from django.db import models

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    date_added = models.DateTimeField("date published")

class Sale(models.Model):
    product_sale = models.ForeignKey(Products, on_delete=models.CASCADE)
    time_sold = models.DateTimeField('time sold')
    quantity_sold = models.IntegerField(default=0)


