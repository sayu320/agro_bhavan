from django import forms
from .models import *
class ProductsForm(forms.ModelForm):
    class Meta :
        model = Shop_Products
        fields = ['name','description','price','quantity','image','product_type']
        widgets = {
            "name" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"name"}),
            "description" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"description"}),
            "price" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"price"}),
            "quantity" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"quantity"}),
            "product_type" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"product_type"}),
        }

class shopprofileForm(forms.ModelForm):
    class Meta :
        fields = ['name','photo']