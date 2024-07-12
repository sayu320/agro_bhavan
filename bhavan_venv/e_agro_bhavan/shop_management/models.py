from django.db import models
from farmer.models import *

class Shop_Products(models.Model):
    uid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)        
    name = models.CharField(max_length=50,default='') 
    description = models.CharField(max_length=150,default='')
    price = models.CharField(max_length=50,default='')
    quantity = models.CharField(max_length=50,default='') 
    image =  models.FileField()
    product_type = models.CharField(max_length=50,default='')
    no_of_remaining_items = models.CharField(max_length=50,default='')
