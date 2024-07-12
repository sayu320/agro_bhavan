from django import forms
from .models import *
from farmer_management.models import*

class SchemeForm(forms.ModelForm):

    class Meta:
        model = Scheme
        fields = ['scheme_name','description','image']    
        widgets = {
            "scheme_name" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"scheme_name"}),
            "description" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"scheme_name"})
        }

class schemeForm(forms.ModelForm):
    class Meta:
        sub_scheme = forms.CharField(required=False)
        model = Sub_scheme
        fields = ['s_id','sub_scheme','document','start_date','expiry_date']
        widgets = {
               
        }
    
    
class ProductForm(forms.ModelForm):
    class Meta :
        model = Products
        fields = ['name','description','price','quantity','Unit','image','product_type']
        widgets = {
            "name" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"name"}),
            "description" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"description"}),
            "price" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"price"}),
            "quantity" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","label":"quantity"}),
            
            "product_type" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"product_type"}),
        }

class NewsForm(forms.ModelForm):
    class Meta :
        model = News
        fields = ['title','content','image']
        widgets = {
            "title" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"title"}),
            "content" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"content"}),
            
            
            
         
        }  

class responseform(forms.ModelForm):
    class Meta :
        model = query
        fields = ['response']
        widgets = {
            "response" : forms.Textarea(attrs={"class":"form-control bg-transparent"}),
            
         
        }  
class OfficerprofileForm(forms.ModelForm):
    class Meta :
        fields =['name','designation','photo']     