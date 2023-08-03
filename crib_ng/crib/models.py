from django.db import models
import datetime
from django.utils import timezone

# Create your models here.
class Products(models.Model):
    product_name = models.CharField(max_length=100)
    quantity = models.IntegerField(default=0)
    date_added = models.DateTimeField("date published")

    def __str__(self):
        return self.product_name
    
    def items_added_time(self):
        return self.date_added >= timezone.now() - datetime.timedelta(days=1)
    

class Sale(models.Model):
    product_sale = models.ForeignKey(Products, on_delete=models.CASCADE)
    time_sold = models.DateTimeField('time sold')
    quantity_sold = models.IntegerField(default=0)


