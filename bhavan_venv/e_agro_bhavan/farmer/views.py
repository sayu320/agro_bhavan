from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from django.contrib.auth.models import User
from django.contrib import auth
import secrets
import string

from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def webpage(request):
    return render(request,'webpage.html')

def index(request):
    return render(request,'index.html')

def contact(request):
    return render(request,'contact.html')  

def about(request):
    return render(request,'about.html')          

def register(request):
    if request.method=='POST':
        form = user_farmerForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user=User.objects.get(username=form.cleaned_data['email'])
                # messages.success(request,'user exists already go to login!!')
                return redirect('/login')
            except User.DoesNotExist:
                user=User.objects.create_user(username=form.cleaned_data['email'],password=form.cleaned_data['password'],is_active="1")
                new_regis = Register.objects.create(
                    name = form.cleaned_data["name"],
                    contact_number = form.cleaned_data["contact_number"],
                    email = form.cleaned_data["email"],
                    password = form.cleaned_data["password"],
                    address = form.cleaned_data["address"],
                    uid = user,
                    usertype="user"
                    )
                auth.login(request,user)
                # messages.success(request,'Signup successful')
                new_regis.save()
            return redirect('/login')
    else:
        form = user_farmerForm()
    return render(request, 'register.html', {'form': form})
    

  
def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST, request.FILES)
        if form.is_valid():
            user = auth.authenticate(request,username=form.cleaned_data['email'],password=form.cleaned_data['password'],is_active="1")
            print(user)
            if user is None:
                return redirect('/login')
            else:

                auth.login(request,user)
                data = Register.objects.get(uid=user)
                print(data)
                request.session['ut'] = data.usertype
                u=data.usertype
                print(u)
                request.session['userid']=data.id
                print(data.id)
                if data.usertype == "farmer":
                    return redirect('/')
                if data.usertype == "user" :
                    return redirect('/')
                if data.usertype == "shops":
                    return redirect('/')
                if data.usertype == "officer":
                    return redirect('/')
                if data.usertype == "admin" :
                    return redirect('/')
            return redirect('/')
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})

def officer(request):
    if request.method=='POST':
        form = user_officerForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user=User.objects.get(username=form.cleaned_data['email'])
                return redirect('/login')
            except User.DoesNotExist:
                user=User.objects.create_user(username=form.cleaned_data['email'],password=form.cleaned_data['password'],is_active="0")
                new_regis = Register.objects.create(
                    name = form.cleaned_data["name"],
                    email = form.cleaned_data["email"],
                    password = form.cleaned_data["password"],
                    photo = form.cleaned_data["photo"],
                    designation = form.cleaned_data["designation"],
                    contact_number = form.cleaned_data["contact_number"],
                    uid = user,
                    usertype="officer"
                    )
                auth.login(request,user)
                new_regis.save()
            return redirect('/login')
    else:
        form = user_officerForm()
    return render(request, 'register.html', {'form': form})


def farmer(request):
    if request.method=='POST':
        print("--------")
        form = user_farmerForm(request.POST, request.FILES)
        if form.is_valid():
            print("---77777-----")
            try:
                user=User.objects.get(username=form.cleaned_data['email'])
                return redirect('/login')
            except User.DoesNotExist:
                print("----8987----")
                user=User.objects.create_user(username=form.cleaned_data['email'],password=form.cleaned_data['password'])
                new_regis = Register.objects.create(
                    name = form.cleaned_data["name"],
                    email = form.cleaned_data["email"],
                    password = form.cleaned_data["password"],
                    contact_number = form.cleaned_data["contact_number"],
                    address = form.cleaned_data["address"],
                    uid = user,
                    usertype="farmer"
                    )
                auth.login(request,user)
                new_regis.save()
            return redirect('/login')
    else:
        form = user_farmerForm()
    return render(request, 'register.html', {'form': form})

def shops(request):
    if request.method=='POST':
        form = user_shopForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                user=User.objects.get(username=form.cleaned_data['email'])
                # messages.success(request,'user exists already go to login!!')
                return redirect('/login')
            except User.DoesNotExist:
                user=User.objects.create_user(username=form.cleaned_data['email'],password=form.cleaned_data['password'],is_active="1")
                new_regis = Register.objects.create(
                    name = form.cleaned_data["name"],
                    email = form.cleaned_data["email"],
                    password = form.cleaned_data["password"],
                    photo = form.cleaned_data["photo"],
                    contact_number = form.cleaned_data["contact_number"],
                    address = form.cleaned_data["address"],
                    type = form.cleaned_data["type"],
                    location = form.cleaned_data["location"],
                    uid = user,
                    usertype="shops"
                    )
                auth.login(request,user)
                # messages.success(request,'Signup successful')
                new_regis.save()
            return redirect('/login')
    else:
        form = user_shopForm()
    return render(request, 'shop_register.html', {'form': form})



def logout(request):
    auth.logout(request)
    return redirect("/")

def view_officers(request):
    a = Register.objects.filter(usertype="officer")
    return render(request,'view_officers.html',{'a':a})

def forgot_password(request):
    msg = ""
    if request.method=="POST":
        form = ForgotForm(request.POST, request.FILES)
        if form.is_valid():
            email=form.cleaned_data['email']
            password_length = 6
            print("1111111111")
            print(secrets.token_urlsafe(password_length))
            print("00000000000")
            password=secrets.token_urlsafe(password_length)
            x = Register.objects.get(email=email)
            print(x)
            k=x.email
            y = User.objects.get(username=email)
            print(x.email)
            l=y.username
            subject = 'YOUR NEW PASSWORD'
            message = password
            print(message)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [x.email]
            send_mail(subject,message,email_from,recipient_list)
            
            if x is None: 
                return render(request,'index.html',{'k':True})
            else:
                x.password = password
                y.set_password(password)
                x.save()
                y.save()
                return redirect('/login')
                
       
    else:
        form = ForgotForm()
    return render(request,'forgot_password.html',{'form':form})  


