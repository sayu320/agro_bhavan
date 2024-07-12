from django.shortcuts import render,redirect
from .forms import *
from farmer_management.models import*
# Create your views here.
from farmer.forms import *

def add_scheme(request):
    c = request.user.id
    print(c)
    form = SchemeForm(request.POST, request.FILES)
    if request.method=='POST':
 
        
        if form.is_valid():
            new_book = Scheme.objects.create(
                uid=Register.objects.get(uid=c),
                scheme_name =form.cleaned_data["scheme_name"],
                description =form.cleaned_data["description"],
                image =form.cleaned_data["image"]
                )
            new_book.save()
            return redirect('/add_sub_scheme')
        else:
            print("999999999999999")
            form = schemeForm()
    return render(request,'add_schemes.html',{'form':form})


def add_sub_scheme(request):
    form = schemeForm(request.POST, request.FILES)
    if request.method=='POST':
        print("----999-----")
        print(form.is_valid())
        if form.is_valid():
            print("---------")
            new_book = Sub_scheme.objects.create(
                s_id=form.cleaned_data["s_id"],
                sub_scheme=form.cleaned_data["sub_scheme"],
                document=form.cleaned_data["document"],
                start_date=form.cleaned_data["start_date"],
                expiry_date=form.cleaned_data["expiry_date"]
                )
            new_book.save()
            return redirect('/')
        else:
            print(form)
            form = schemeForm()
    return render(request,'sub_schemes.html',{'form': form})

def products(request):
    d=request.user
    if request.method=='POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            
            new_regis = Products.objects.create(
                uid = Register.objects.get(uid=d),
                name = form.cleaned_data["name"],
                description = form.cleaned_data["description"],
                price = form.cleaned_data["price"],
                quantity = form.cleaned_data["quantity"],
                image = form.cleaned_data["image"],
                product_type = form.cleaned_data["product_type"],
                )
            new_regis.save()
            return redirect('/')
    else:
        form = ProductForm()
    return render(request, 'add_products.html', {'form': form})

def view_sub_schemes(request):
    a = Sub_scheme.objects.all()
    return render(request,'view_sub_schemes.html',{'a':a})

def edit_scheme(request,id):
    data=Sub_scheme.objects.get(id=id)
    if request.method=='POST':
        form = schemeForm(request.POST,request.FILES, instance=data)
        if form.is_valid():
            print("valid")
            form.save()
        return redirect("/view_sub_schemes",{'data':data})
    else:
        form = schemeForm(instance=data)
        context={
            'form' : form
        }
    return render(request,'edit_schemes.html',context)

def delete_schemes(request,id):
    data = Sub_scheme.objects.get(id=id)
    data.delete()
    return redirect("/view_sub_schemes")

def view_add_products(request):
    a = Products.objects.filter(uid=request.session['userid'])
    return render(request,'view_add_products.html',{'a':a})

def edit_products(request,id):
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
    return render(request,'edit_products.html',context)

def delete_products(request,id):
    data = Products.objects.get(id=id)
    data.delete()
    return redirect("/view_add_products")

def add_news(request):
    d=request.user
    print(d)
    form = NewsForm(request.POST, request.FILES)
    if request.method=='POST':
        print("2222")
        if form.is_valid():
            print("11111111")
            new_regis = News.objects.create(
                uid = Register.objects.get(uid=d),
                title = form.cleaned_data["title"],
                content = form.cleaned_data["content"],
                image = form.cleaned_data["image"],
                
                )
            new_regis.save()
            return redirect('/')
    else:
        form = NewsForm()
    return render(request,'add_news.html', {'form': form})

def view_add_news(request):
    a = News.objects.all()
    return render(request,'view_add_news.html',{'a':a})

def edit_news(request,id):
    data=News.objects.get(id=id)
    if request.method=='POST':
        form = NewsForm(request.POST,request.FILES, instance=data)
        if form.is_valid():
            print("valid")
            form.save()
        return redirect("/view_add_news",{'data':data})
    else:
        form = NewsForm(instance=data)
        context={
            'form' : form
        }
    return render(request,'edit_news.html',context)

def delete_news(request,id):
    data = News.objects.get(id=id)
    data.delete()
    return redirect("/view_add_news")

def view_booking(request):
    c=Register.objects.get(id=request.session['userid'])
    a = product_booking.objects.filter(pid__uid=c)
    return render(request,'view_booking.html',{'a':a})

def view_query(request):
    c=Register.objects.get(id=request.session['userid'])
    k=c.id
    print(c.id)
    a = query.objects.all()
    return render(request,'view_query.html',{'a':a})    

def response(request,id):
    if request.method=='POST':
        form = responseform(request.POST, request.FILES)
    
        print("2222")
        
        if form.is_valid():
            c=query.objects.get(id=id)
            c.response = form.cleaned_data["response"]
            c.save()
            return redirect('/')   
    else:
        form = responseform()
    return render(request,'response.html', {'form': form})

def profile(request):
    i=Register.objects.get(id=request.session['userid'])
    return render(request,'profile.html',{'i':i})
    
def edit_profile(request):
    print("-------1--------")
    print(request.session['userid'])
    data=Register.objects.get(id=request.session['userid'])
    data1=User.objects.get(id=request.user.id)
    if request.method=='POST':
        form = user_officerForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            print("valid")
            data1.set_password(form.cleaned_data['password'])
            data1.save
            form.save()
        return redirect("/profile",{'data':data})
    else: 
        form = user_officerForm(instance=data)
        context={
            'form' : form
        }
    return render(request,'edit_profile.html',context)
      


def view_applied_schemes(request):
    a = Apply_FY_plan.objects.all()
    return render(request,'view_applied_schemes.html',{'a':a})  




def vw_insurance_book(request):
    a = Apply_Insurance.objects.all()
    return render(request,'vw_insurance_book.html',{'a':a})  


def vw_electri_book(request):
    a = Apply_Electricity.objects.all()
    return render(request,'vw_electri_book.html',{'a':a})  


def vw_pension_book(request):
    a = Apply_Pension.objects.all()
    return render(request,'vw_pension_book.html',{'a':a})  


def vw_state_h_m_book(request):
    a = Apply_Pension.objects.all()
    return render(request,'vw_state_h_m_book.html',{'a':a})  


def vw_pm_k_book(request):
    a = Apply_Pradhan_Manthri_Kisan.objects.all()
    return render(request,'vw_pm_k_book.html',{'a':a})  

def edit_officer(request):
    print("-------1--------")
    print(request.session['userid'])
    data=Register.objects.get(id=request.session['userid'])
    data1=User.objects.get(id=request.user.id)
    if request.method=='POST':
        form = user_officerForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            print("valid")
            data1.set_password(form.cleaned_data['password'])
            data1.save
            form.save()
        return redirect("/profile",{'data':data})
    else: 
        form = user_officerForm(instance=data)
        context={
            'form' : form
        }
    return render(request,'edit_profile.html',context)

def edit_farmer(request):
    print("-------1--------")
    print(request.session['userid'])
    data=Register.objects.get(id=request.session['userid'])
    data1=User.objects.get(id=request.user.id)
    if request.method=='POST':
        form = user_farmerForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            print("valid")
            data1.set_password(form.cleaned_data['password'])
            data1.save
            form.save()
        return redirect("/profile",{'data':data})
    else: 
        form = user_farmerForm(instance=data)
        context={
            'form' : form
        }
    return render(request,'edit_profile.html',context)

def edit_shops(request):
    print("-------1--------")
    print(request.session['userid'])
    data=Register.objects.get(id=request.session['userid'])
    data1=User.objects.get(id=request.user.id)
    if request.method=='POST':
        form = user_shopForm(request.POST,request.FILES,instance=data)
        if form.is_valid():
            print("valid")
            data1.set_password(form.cleaned_data['password'])
            data1.save
            form.save()
        return redirect("/profile",{'data':data})
    else: 
        form = user_shopForm(instance=data)
        context={
            'form' : form
        }
    return render(request,'edit_profile.html',context)    
