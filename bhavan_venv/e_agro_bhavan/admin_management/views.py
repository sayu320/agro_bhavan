from django.shortcuts import render
from farmer.models import *

# Create your views here.
def view_user(request):
    a = Register.objects.all()
    return render(request,'view_users.html',{'a':a})
def appro(request,id):
    res = register.objects.get(id=id)
    user = res.uid
    user.is_active = True
    user.save()
    return redirect("/approval")
def approval(request):
    a = register.objects.filter(uid__is_active=False).all()
    print(a)
    
    
    return render(request,'approval.html',x)
