from django.shortcuts import render,redirect
from officer_management.models import *
from .forms import *
from .models import *
import datetime
# Create your views here.
def view_schemes(request):
    a = Scheme.objects.all()
    return render(request,'view_schemes.html',{'a':a})

def products(request):
    a=Products.objects.all()
    return render(request,'products.html',{'a':a})
    


def apply_now(request,id):
    a=Sub_scheme.objects.get(id=id)
    d=request.user
    if request.method=='POST':
        form = applyForm(request.POST, request.FILES)
        if form.is_valid():
            
            Apply_Insurance.objects.create(
                uid = Register.objects.get(uid=d),
                sid = Sub_scheme.objects.get(id=a),
                house_name = form.cleaned_data["house_name"],
                street_name = form.cleaned_data["street_name"],
                place = form.cleaned_data["place"],
                pin_code = form.cleaned_data["pin_code"],
                ration_card_no = form.cleaned_data["ration_card_no"],
                total_land_owned = form.cleaned_data["total_land_owned"],
                total_farming_land_owned = form.cleaned_data["total_farming_land_owned"],
                date_on_which_crop_failure_occured = form.cleaned_data["date_on_which_crop_failure_occured"],
                reason_for_crop_failure = form.cleaned_data["reason_for_crop_failure"],
                village = form.cleaned_data["village"],
                survey_no = form.cleaned_data["survey_no"],
                sub_division_no = form.cleaned_data["sub_division_no"],
                area_or_number_of_crops = form.cleaned_data["area_or_number_of_crops"],
                damage_details = form.cleaned_data["damage_details"],
                damaged_crop = form.cleaned_data["damaged_crop"],
                phase_in_which_the_crops_damaged = form.cleaned_data["phase_in_which_the_crops_damaged"],
                farming_expenditure = form.cleaned_data["farming_expenditure"],
                expected_income_from_crops = form.cleaned_data["expected_income_from_crops"],
                required_document_for_submission = form.cleaned_data["required_document_for_submission"],
                date_of_applying = datetime.today()
                )
            return redirect('/')
    else:
        form = applyForm()
    return render(request,'apply now.html',{'a':a,'form':form})

def fy_apply_now(request):
    d=request.user
    if request.method=='POST':
        form = Apply_FY_form(request.POST, request.FILES)
        if form.is_valid():
            Apply_FY_plan.objects.create(
                uid = Register.objects.get(uid=d),
                scheme_name = form.cleaned_data["scheme_name"],
                house_no = form.cleaned_data["house_no"],
                age_of_the_applicant = form.cleaned_data["age_of_the_applicant"],
                ration_card_no = form.cleaned_data["ration_card_no"],
                category = form.cleaned_data["category"],
                permanent_resident = form.cleaned_data["permanent_resident"],
                annual_income = form.cleaned_data["annual_income"],
                irrigation_facility = form.cleaned_data["irrigation_facility"],
                own_house = form.cleaned_data["own_house"],
                wasteland = form.cleaned_data["wasteland"],
                hut = form.cleaned_data["hut"],
                floor_area = form.cleaned_data["floor_area"],
                ownership_of_the_house = form.cleaned_data["ownership_of_the_house"],
                roof_of_the_house = form.cleaned_data["roof_of_the_house"],
                wall_of_the_house = form.cleaned_data["wall_of_the_house"],
                floor_of_the_house = form.cleaned_data["floor_of_the_house"],
                drinking_water = form.cleaned_data["drinking_water"],
                age_of_the_house = form.cleaned_data["age_of_the_house"],
                toilet = form.cleaned_data["toilet"],
                required_document_for_submission = form.cleaned_data["required_document_for_submission"],
                date_of_applying = datetime.today()
                )
            return redirect('/')
    else:
        form = Apply_FY_form()
    return render(request,'apply now.html',{'form':form})


                      

def view_subscheme(request,id):
    a = Sub_scheme.objects.filter(s_id=id)
    return render(request,'view_subscheme.html',{'a':a})



def apply_ele(request,id):
    a=Scheme.objects.get(id=id)
    d=request.user
    if request.method=='POST':
        form = apply_electri(request.POST, request.FILES)
        if form.is_valid():
            Apply_Electricity.objects.create(
                uid = Register.objects.get(uid=d),
                name_of_krishibhavan = form.cleaned_data["name_of_krishibhavan"],
                place = form.cleaned_data["place"],
                house_number = form.cleaned_data["house_number"],
                village = form.cleaned_data["village"],
                survey_number = form.cleaned_data["survey_number"],
                land_area = form.cleaned_data["land_area"],
                farm_area = form.cleaned_data["farm_area"],
                name_of_the_crops = form.cleaned_data["name_of_the_crops"],
                number_or_area_of_the_crops = form.cleaned_data["number_or_area_of_the_crops"],
                horse_power = form.cleaned_data["horse_power"],
                KSEB_consumer_number = form.cleaned_data["KSEB_consumer_number"],
                monthly_amount = form.cleaned_data["monthly_amount"],
                required_document_for_submission = form.cleaned_data["required_document_for_submission"],
                date_of_applying = datetime.datetime.today()
            )   
            return redirect('/')
    else:
        form = apply_electri()
    return render(request,'apply now.html',{'form':form}) 


def apply_pen(request,id):
    a=Scheme.objects.get(id=id)
    d=request.user
    if request.method=='POST':
        form = apply_pens(request.POST, request.FILES)
        if form.is_valid():
            Apply_Pension.objects.create(
                uid = Register.objects.get(uid=d),
                district = form.cleaned_data["district"],
                block = form.cleaned_data["block"],
                name_of_krishibhavan = form.cleaned_data["name_of_krishibhavan"],
                pin_code = form.cleaned_data["pincode"],
                gender = form.cleaned_data["gender"],
                category = form.cleaned_data["category"],
                village = form.cleaned_data["village"],
                survey_number = form.cleaned_data["survey_number"],
                land_area = form.cleaned_data["land_area"],
                farming_details = form.cleaned_data["farming_details"],
                years_of_experience = form.cleaned_data["years_of_experience"],
                account_number = form.cleaned_data["account_number"],
                bank_name = form.cleaned_data["bank_name"],
                branch_name = form.cleaned_data["branch_name"],
                required_document_for_submission = form.cleaned_data["required_document_for_submission"],
                date_of_applying = datetime.datetime.today()
            )   
            return redirect('/')
    else:
        form = apply_pens()
    return render(request,'apply now.html',{'form':form}) 

def apply_SHM(request,id):
    a=Scheme.objects.get(id=id)
    d=request.user
    if request.method=='POST':
        form = apply_State_HM(request.POST, request.FILES)
        if form.is_valid():
            Apply_State_Horticulture_Mission.objects.create(
                uid = Register.objects.get(uid=d),
                name_of_krishibhavan = form.cleaned_data["name_of_krishibhavan"],
                scheme_name = form.cleaned_data["scheme_name"],
                gender = form.cleaned_data["gender"],
                category = form.cleaned_data["category"],
                local_body = form.cleaned_data["local_body"],
                ward_name = form.cleaned_data["ward_name"],
                district = form.cleaned_data["district"],
                block = form.cleaned_data["block"],
                village = form.cleaned_data["village"],
                survey_number = form.cleaned_data["survey_number"],
                total_land = form.cleaned_data["total_land"],
                bank_loan = form.cleaned_data["bank_loan"],
                bank_name = form.cleaned_data["bank_name"],
                account_number = form.cleaned_data["account_number"],
                required_document_for_submission = form.cleaned_data["required_document_for_submission"],
                date_of_applying = datetime.datetime.today()
            )   
            return redirect('/')
    else:
        form = apply_State_HM()
    return render(request,'apply now.html',{'form':form})

def apply_PMK(request,id):
    a=Scheme.objects.get(id=id)
    d=request.user
    if request.method=='POST':
        form = apply_PM_kisan(request.POST, request.FILES)
        if form.is_valid():
            Apply_Pradhan_Manthri_Kisan.objects.create(
                uid = Register.objects.get(uid=d),
                name_of_krishibhavan = form.cleaned_data["name_of_krishibhavan"],
                block = form.cleaned_data["block"],
                district = form.cleaned_data["district"],
                village = form.cleaned_data["village"],
                fathers_name = form.cleaned_data["fathers_name"],
                post_office = form.cleaned_data["post_office"],
                pin_code = form.cleaned_data["pin_code"],
                category = form.cleaned_data["category"],
                date_of_birth = form.cleaned_data["date_of_birth"],
                ration_card_number = form.cleaned_data["ration_card_number"],
                bank_account_number = form.cleaned_data["bank_account_number"],
                bank_name = form.cleaned_data["bank_name"],
                branch = form.cleaned_data["branch"],
                IFSC_code = form.cleaned_data["IFSC_code"],
                survey_number = form.cleaned_data["survey_number"],
                land_area = form.cleaned_data["land_area"],
                thaluk = form.cleaned_data["thaluk"],
                required_document_for_submission = form.cleaned_data["required_document_for_submission"],
                date_of_applying = datetime.datetime.today()
            )   
            return redirect('/')
    else:
        form = apply_PM_kisan()
    return render(request,'apply now.html',{'form':form})


def req_query(request):
    d=request.user
    if request.method=='POST':
        form = query_manage(request.POST, request.FILES)
        if form.is_valid():
            
            query.objects.create(
                uid = Register.objects.get(uid=d),
                description = form.cleaned_data["description"],
                image = form.cleaned_data["image"],
            

            )    
            return redirect('/')
    else:
        form = query_manage()
    return render(request,'query_management.html',{'form':form}) 

def view_products(request):
    a = Products.objects.all()
    return render(request,'view_products.html',{'a':a})

def book_prod(request,id):
    d=request.user
    if request.method=='POST':
        form = book_products(request.POST, request.FILES)
        if form.is_valid():
            pid = Products.objects.get(id=id)
            n = pid.Unit
            l = int(pid.quantity)
            print(l)
            h = pid.price
            print(h)
            quantity = form.cleaned_data["quantity"]
            j = int(pid.price) * int(quantity)
            print(j)
            if int(quantity) > l:
                return render(request,'index.html',{'t':True})
            else:
                k = int(l) - int(quantity)
                pid.quantity = k
                pid.save()
            
            
                product_booking.objects.create(
                    uid = Register.objects.get(uid=d),
                    pid = Products.objects.get(id=id),
                    date = form.cleaned_data["date"],
                    quantity = form.cleaned_data["quantity"],
                    amount =j
                    )    
                return redirect('/')
        
    else:
        form = book_products()
    return render(request,'booking.html',{'form':form}) 

def news(request):
    a = News.objects.all()
    return render(request,'news.html',{'a':a})

def profile(request):
    i=Register.objects.get(id=request.session['userid'])
    return render(request,'profile.html',{'i':i})
