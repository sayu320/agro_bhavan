from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Register(models.Model):
    uid = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=50,default='')
    contact_number = models.IntegerField(max_length=50,default='')
    photo = models.FileField(null=True)
    designation = models.CharField(max_length=50,default='')
    email = models.CharField(max_length=50,default='')
    password = models.CharField(max_length=50,default='')
    address = models.CharField(max_length=50,default='')
    usertype = models.CharField(max_length=50,default='')
    type = models.CharField(max_length=50,default='')
    location = models.CharField(max_length=50,default='')
    panchayath = models.CharField(max_length=50,default='')
    aadhar_number =  models.IntegerField(default=0) 
    ward =  models.IntegerField(default=0)