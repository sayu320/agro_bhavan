from django.shortcuts import render,redirect
from .forms import *
from.models import *
from officer_management.models import *

def prod(request):
    d=request.user
    print("hiiiiiiiiiiiiiiiiiiiiiiiii")
    print(request.method=='POST')
    if request.method=='POST':
        print("hiiiiiii")
        form = ProductsForm(request.POST, request.FILES)
        print(form.is_valid())
        if form.is_valid():
            print("111111")
            
            new_regis = Products.objects.create(
                uid = Register.objects.get(uid=d),
                name = form.cleaned_data["name"],
                description = form.cleaned_data["description"],
                price = form.cleaned_data["price"],
                quantity = form.cleaned_data["quantity"],
                image = form.cleaned_data["image"],
                product_type = form.cleaned_data["product_type"],
                no_of_remaining_items = form.cleaned_data["no_of_remaining_items"]
                )
            new_regis.save()
            return redirect('/')
    else:
        print("00000000000")
        form = ProductsForm()
    return render(request,'add_products.html',{'form': form})

def view_add_prod(request):
    c=Register.objects.get(id=request.session['userid'])
    k=c.id
    print(c.id)
    a = Products.objects.filter(uid=c)
    print(request.session['userid'])
    return render(request,'view_add_products.html',{'a':a})

def edit_add_prod(request,id):
    data=Products.objects.get(id=id)
    if request.method=='POST':
        form = ProductForm(request.POST,request.FILES, instance=data)
        if form.is_valid():
            print("valid")
            form.save()
        return redirect("/view_add_products",{'data':data})
    else:
        form = ProductForm(instance=data)
        context={
            'form' : form
        }
    return render(request,'edit_add_products.html',context)

def profile(request):
    i=Register.objects.get(id=request.session['userid'])
    
    return render(request,'profile.html',{'i':i})    
