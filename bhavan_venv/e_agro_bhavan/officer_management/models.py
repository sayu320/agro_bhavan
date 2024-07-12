from django.db import models
from farmer.models import *
# Create your models here.
class Scheme(models.Model):
    uid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    scheme_name = models.CharField(max_length=50,default='')
    description = models.CharField(max_length=500,default='')
    image =  models.FileField(null=True)
    def __str__(self) -> str:
        return self.scheme_name 

class Sub_scheme(models.Model):
    s_id = models.ForeignKey(Scheme,on_delete=models.CASCADE,null=True)
    sub_scheme = models.CharField(max_length=50,default='', null= True)
    document = models.FileField(null=True)
    start_date = models.DateField(null=True)
    expiry_date = models.DateField(null=True)


Unit=[
    ('Kg','Kg'),
    ('g','g'),
    ('ml','ml'),
    ('L','L'),
    ('peice','peice')
]
class Products(models.Model):
    uid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)        
    name = models.CharField(max_length=50,default='') 
    description = models.CharField(max_length=50,default='')
    price = models.CharField(max_length=50,default='')
    quantity = models.CharField(max_length=50,default='') 
    Unit = models.CharField('Unit',choices=Unit,default='peice',max_length=250)
    image =  models.FileField()
    product_type = models.CharField(max_length=50,default='')
    no_of_remaining_items = models.CharField(max_length=50,default='',null=True)

class News(models.Model):
    uid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True) 
    title = models.CharField(max_length=50,default='') 
    content = models.CharField(max_length=150,default='')   
    image = models.FileField() 
    

