from django import forms
from .models import *

class applyForm(forms.ModelForm):
    class Meta:
        model = Apply_Insurance
        fields = ['house_name','street_name','place','pin_code','ration_card_no','total_land_owned','total_farming_land_owned','date_on_which_crop_failure_occured','reason_for_crop_failure','village','survey_no','sub_division_no','area_or_number_of_crops','damage_details','damaged_crop','phase_in_which_the_crops_damaged','farming_expenditure','expected_income_from_crops','required_document_for_submission']
        widgets= {
            "house_name": forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "street_name": forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "place": forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "pin_code": forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "ration_card_no": forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "total_land_owned": forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "total_farming_land_owned": forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "date_on_which_crop_failure_occured": forms.TextInput(attrs={"class":"","type":"date","style":"width:100%"}),
            "reason_for_crop_failure": forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "village": forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "survey_no": forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "subdivision_no": forms.TextInput(attrs={"class":"form-control bg-transparent","style":"margin-left:100%"}),
            "area_or_number_of_crops": forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "damage_details": forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "damaged_crop": forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "phase_in_which_crops_damaged": forms.TextInput(attrs={"class":"form-control bg-transparent","style":"margin-left:100%"}),
            "farming_expenditure": forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "expected_income_from_crops": forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "required_document_for_submission": forms.TextInput(attrs={"class":"form-control bg-transparent"}),


            
             }

 

class Apply_FY_form(forms.ModelForm):
    class Meta:
        model = Apply_FY_plan
        fields = ['scheme_name','house_no','age_of_the_applicant','ration_card_no','category','permanent_resident','annual_income','irrigation_facility','own_house','wasteland','hut','floor_area','ownership_of_the_house','roof_of_the_house','wall_of_the_house','floor_of_the_house','drinking_water','age_of_the_house','toilet','required_document_for_submission']
        widgets= {

            "house_no": forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "age_of_the_applicant": forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "ration_card_no": forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "scheme_name" : forms.Select(attrs={"class":"form-control bg-transparent"}),
            "category" : forms.Select(attrs={"class":"form-control bg-transparent"}),
            "floor_area": forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "annual_income": forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "permanent_resident" : forms.Select(attrs={"class":"form-control bg-transparent"}),
            "irrigation_facility" : forms.Select(attrs={"class":"form-control bg-transparent"}),
            "own_house" : forms.Select(attrs={"class":"form-control bg-transparent"}),
            "wasteland" : forms.Select(attrs={"class":"form-control bg-transparent"}),
            "hut" : forms.Select(attrs={"class":"form-control bg-transparent"}),
            "ownership_of_the_house" : forms.Select(attrs={"class":"form-control bg-transparent"}),
            "roof_of_the_house" : forms.Select(attrs={"class":"form-control bg-transparent"}),
            "wall_of_the_house" : forms.Select(attrs={"class":"form-control bg-transparent"}),
            "floor_of_the_house" : forms.Select(attrs={"class":"form-control bg-transparent"}),
            "drinking_water" : forms.Select(attrs={"class":"form-control bg-transparent"}),
            "age_of_the_house" : forms.Select(attrs={"class":"form-control bg-transparent"}),
            "toilet" : forms.Select(attrs={"class":"form-control bg-transparent"}),
             
        }


class apply_electri(forms.ModelForm):        
    class Meta:
        model = Apply_Electricity
        fields = ['name_of_krishibhavan','place','house_number','village','survey_number','land_area','farm_area','name_of_the_crops','number_or_area_of_the_crops','horse_power','KSEB_consumer_number','monthly_amount','required_document_for_submission']
        widgets = {
            "name of krishi bhavan" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "place" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "house number" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "survey number" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "village" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "survey number" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "land area" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "farm area" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "name of the crops" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "number or area of the crops" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "horse power" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "KSEB consumer number" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "monthly amount" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "documents required for submission" : forms.TextInput(attrs={"class":"form-control bg-transparent"})
        }        

class apply_pens(forms.ModelForm):        
    class Meta:
        model = Apply_Pension
        fields = ['district','block','name_of_krishibhavan','pincode','gender','category','village','survey_number','land_area','farming_details','years_of_experience','account_number','bank_name','branch_name','required_document_for_submission']
        widgets = {
            "district" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "block" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "name of krishi bhavan" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "pincode" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "gender" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "category" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "village" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "survey number" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "land area" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "farming details" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "name of the crops" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "years of experience" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "account number" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "bank name" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "branch name" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "documents required for submission" : forms.TextInput(attrs={"class":"form-control bg-transparent"})
        }         

class apply_State_HM(forms.ModelForm):        
    class Meta:
        model = Apply_State_Horticulture_Mission
        fields = ['name_of_krishibhavan','scheme_name','gender','category','local_body','ward_name','block','district','village','survey_number','total_land','bank_loan','bank_name','account_number','required_document_for_submission']
        widgets = {
            "name of krishi bhavan" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "scheme name" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "gender" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "category" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "local body" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "ward name" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "block" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "district" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "village" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "survey number" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "total land" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "bank loan" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "bank name" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "account number" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "documents required for submission" : forms.TextInput(attrs={"class":"form-control bg-transparent"})
        }         

class apply_PM_kisan(forms.ModelForm):        
    class Meta:
        model = Apply_Pradhan_Manthri_Kisan
        fields = ['name_of_krishibhavan','block','district','village','fathers_name','post_office','pin_code','category','date_of_birth','ration_card_number','bank_account_number','bank_name','branch_name','IFSC_code','survey_number','land_area','thaluk','required_document_for_submission']
        widgets = {
            "name of krishi bhavan" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "block" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "district" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "village" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "fathers name" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "post office" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "pin code" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "category" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "date of birth" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "ration card number" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "bank account number" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "bank name" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "branch" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "IFSC code" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "survey number" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "land area" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "thaluk" : forms.TextInput(attrs={"class":"form-control bg-transparent"}),
            "documents required for submission" : forms.TextInput(attrs={"class":"form-control bg-transparent"})
        }         

class query_manage(forms.ModelForm):        
    class Meta:
        model = query
        fields = ['description','image',] 
        widgets = {
            "description" : forms.TextInput(attrs={"class":"form-control bg-transparent phn","type":"description"}),

        }       
class book_products(forms.ModelForm):
    class Meta:
        model = product_booking
        fields = ['date','quantity'] 
        widgets = {
            "date" : forms.TextInput(attrs={"class":"form-control bg-transparent","type":"date"}),
            "quantity" : forms.TextInput(attrs={"class":"form-control bg-transparent"})
         
        }       
class farmerprofileForm(forms.ModelForm):
    class Meta:
        fields = ['name','photo']            