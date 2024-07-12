from django import forms
from .models import *





class user_farmerForm(forms.ModelForm):

    class Meta:
        model = Register
        fields = ['name','contact_number','email','password','photo','address','panchayath','aadhar_number','ward']
        widgets = {
          "name" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"name"}),
          "contact_number" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"contact number"}),
          "email" : forms.EmailInput(attrs={"class":"form-control bg-transparent email"}),
          "password" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"password"}),
          
          "address" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"address"}),
          "panchayath" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"panchayath"}),
          "aadhar_number" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"aadhar number"}),
          "ward" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"ward"}),
        }  

class user_officerForm(forms.ModelForm):

    class Meta:
        model = Register
        fields = ['name','contact_number','email','password','photo','designation']        
        widgets = {
          "name" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"name"}),
          "contact_number" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"contact number"}),
          "email" : forms.EmailInput(attrs={"class":"form-control bg-transparent email"}),
          "password" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"password"}),
          "designation" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"designation"}),
        }  

class LoginForm(forms.ModelForm):

    class Meta:
        model = Register
        fields = ['email','password']
        widgets = {
          "password" : forms.PasswordInput(attrs={"class":"form-control bg-transparent","type":"password"}),
          "email" : forms.EmailInput(attrs={"class":"form-control bg-transparent email"})
        }       
       



class ForgotForm(forms.ModelForm):

    class Meta:
        model = Register
        fields = ['email']
        widgets = {
         
        }       
       

class user_shopForm(forms.ModelForm):

    class Meta:
        model = Register
        fields = ['name','password','photo','type','address','contact_number','email','location']    
        widgets = {
          "name" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"name"}),
          "password" : forms.PasswordInput(attrs={"class":"form-control bg-transparent","type":"password"}),
          "email" : forms.EmailInput(attrs={"class":"form-control bg-transparent email"}),
          "contact_number" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"contact number"}),
          "type" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"type"}),
          "address" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"address"}),
          "location" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"location"}),

    
        }       
       