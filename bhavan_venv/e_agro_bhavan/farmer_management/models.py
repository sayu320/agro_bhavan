from django.db import models
from farmer.models import *
from officer_management.models import *
# Create your models here.
class Apply_Insurance(models.Model):
    uid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    sid = models.ForeignKey(Sub_scheme,on_delete=models.CASCADE,null=True)
    house_name = models.CharField(max_length=50,default='') 
    street_name = models.CharField(max_length=50,default='') 
    place = models.CharField(max_length=50,default='') 
    pin_code = models.IntegerField(max_length=50,default=0)
    ration_card_no = models.IntegerField(max_length=50,default=0)
    total_land_owned = models.CharField(max_length=50,default='')
    total_farming_land_owned = models.CharField(max_length=50,default='')
    date_on_which_crop_failure_occured = models.DateField(null=True)
    reason_for_crop_failure = models.CharField(max_length=50,default='')
    village = models.CharField(max_length=50,default='')
    survey_no = models.IntegerField(max_length=50,default=0)
    sub_division_no = models.IntegerField(max_length=50,default=0)
    area_or_number_of_crops = models.CharField(max_length=50,default='')
    damage_details = models.CharField(max_length=50,default='')
    damaged_crop = models.CharField(max_length=50,default='')
    phase_in_which_the_crops_damaged = models.CharField(max_length=50,default='')
    farming_expenditure = models.CharField(max_length=50,default='')
    expected_income_from_crops = models.CharField(max_length=50,default='')
    required_document_for_submission = models.FileField(null=True)
    date_of_applying = models.DateField(null=True)

SCHEME_NAME=[
    ('Comprehensive Coconut Cultivation Development','Comprehensive Coconut Cultivation Development'),
    ('Modern vegetable cultivation','Modern vegetable cultivation'),
    ('Growing vegetables in pots','Growing vegetables in pots')
]
CATEGORY=[
    ('General','General'),
    ('Minority','Minority'),
    ('Others','Others')
]    
PERMANENT_RESIDENT=[
    ('Yes','Yes'),
    ('No','No')
]
IRRIGATION_FACILITY=[
    ('Yes','Yes'),
    ('No','No')
]
OWN_HOUSE=[
    ('Yes','Yes'),
    ('No','No')
]
WASTELAND=[
    ('Yes','Yes'),
    ('No','No')
]
HUT=[
    ('Yes','Yes'),
    ('No','No')
]
OWNERSHIP_OF_THE_HOUSE=[
    ('Own','Own'),
    ('Rent','Rent'),
    ('Joint Family','Joint Family'),
    ('Relative House','Relative House'),
    ('Wasteland','Wasteland'),
    ('Others','Others')
]
ROOF_OF_THE_HOUSE=[
    ('Terrace','Terrace'),
    ('Coconut_Leaf','Coconut_Leaf'),
    ('Grass','Grass'),
    ('Sun Dried tiles','Sun Dried tiles'),
    ('Concrete','Concrete')
]
WALL_OF_THE_HOUSE=[
    ('Bricks','Bricks'),
    ('Coconut Leaf','Coconut Leaf'),
    ('Mud','Mud'),
    ('Laterite Stone','Laterite Stone'),
    ('Holobricks','Holobricks')
]
FLOOR_OF_THE_HOUSE=[
    ('Sand','Sand'),
    ('Cement','Cement'),
    ('Tiles','Tiles'),
    ('Mosaic','Mosaic'),
    ('Marble','Marble')
]
DRINKING_WATER=[
    ('Own Well','Own Well'),
    ('Public Well','Public Well'),
    ('Pond','Pond'),
    ('Public tap','Public tap')
]
AGE_OF_THE_HOUSE=[
    ('Less Than 12 Years','Less Than 12 Years'),
    ('More Than 12 Years','More Than 12 Years')
]
TOILET=[
    ('Yes','Yes'),
    ('No','No')
]
class Apply_FY_plan(models.Model):
    uid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    scheme_name =  models.CharField('Scheme name',choices=SCHEME_NAME,default='Comprehensive Coconut Cultivation Development',max_length=250)
    house_no = models.IntegerField(max_length=50)
    age_of_the_applicant = models.IntegerField(max_length=50)
    ration_card_no = models.IntegerField(max_length=50)
    category = models.CharField('Category',choices=CATEGORY,default='General',max_length=250)
    permanent_resident = models.CharField('Permanent resident',choices=PERMANENT_RESIDENT,default='Yes',max_length=250)
    annual_income = models.IntegerField(max_length=50)
    irrigation_facility = models.CharField('Irrigation facility',choices=IRRIGATION_FACILITY,default='Yes',max_length=250)
    own_house = models.CharField('Own house',choices=OWN_HOUSE,default='Yes',max_length=250)
    wasteland = models.CharField('Wasteland',choices=WASTELAND,default='No',max_length=250)
    hut = models.CharField('Hut',choices=HUT,default='No',max_length=250)
    floor_area = models.CharField(max_length=50,default='') 
    ownership_of_the_house = models.CharField('Ownership of the house',choices=OWNERSHIP_OF_THE_HOUSE,default='Own',max_length=250)
    roof_of_the_house = models.CharField('Roof of the house',choices=ROOF_OF_THE_HOUSE,default='Terrace',max_length=250)
    wall_of_the_house = models.CharField('Wall of the house',choices=WALL_OF_THE_HOUSE,default='Holobricks',max_length=250)
    floor_of_the_house = models.CharField('Floor of the house',choices=FLOOR_OF_THE_HOUSE,default='Tiles',max_length=250)
    drinking_water = models.CharField('Drinking water',choices=DRINKING_WATER,default='Own well',max_length=250)
    age_of_the_house = models.CharField('Age of the house',choices=AGE_OF_THE_HOUSE,default='Less than 12 years',max_length=250)
    toilet = models.CharField('Toilet',choices=TOILET,default='Yes',max_length=250)
    required_document_for_submission = models.FileField(null=True)
    date_of_applying = models.DateField(null=True)


class Apply_Electricity(models.Model):
    uid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    name_of_krishibhavan = models.CharField(max_length=50,default='') 
    place = models.CharField(max_length=50,default='') 
    house_number = models.IntegerField(max_length=50,default=0)
    village = models.CharField(max_length=50,default='')
    survey_number = models.IntegerField(max_length=50,default=0)
    land_area = models.CharField(max_length=50,default='')
    farm_area = models.CharField(max_length=50,default='')
    name_of_the_crops = models.CharField(max_length=50,default='')
    number_or_area_of_the_crops = models.CharField(max_length=50,default='')
    horse_power = models.CharField(max_length=50,default='')
    KSEB_consumer_number = models.IntegerField(max_length=50,default=0)
    monthly_amount = models.CharField(max_length=50,default='')
    required_document_for_submission = models.FileField(null=True)
    date_of_applying = models.CharField(max_length=150,default='')

class Apply_Pension(models.Model):
    uid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    district = models.CharField(max_length=50,default='') 
    block = models.CharField(max_length=50,default='') 
    name_of_krishibhavan = models.CharField(max_length=50,default='')
    pincode = models.IntegerField(max_length=50,default=0) 
    gender = models.CharField(max_length=50,default='')
    category = models.CharField(max_length=50,default='')
    village = models.CharField(max_length=50,default='')
    survey_number = models.IntegerField(max_length=50,default=0)
    land_area = models.CharField(max_length=50,default='')
    farming_details = models.CharField(max_length=50,default='')
    years_of_experience = models.CharField(max_length=50,default='')
    account_number = models.IntegerField(max_length=50,default='')
    bank_name = models.CharField(max_length=50,default='')
    branch_name = models.CharField(max_length=50,default='')
    required_document_for_submission = models.FileField(null=True)

class Apply_State_Horticulture_Mission(models.Model):
    uid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    name_of_krishibhavan = models.CharField(max_length=50,default='')
    scheme_name = models.CharField(max_length=50,default='') 
    gender = models.CharField(max_length=50,default='')
    category = models.CharField(max_length=50,default='')
    local_body = models.CharField(max_length=50,default='')
    ward_name = models.CharField(max_length=50,default='')
    block = models.CharField(max_length=50,default='') 
    district = models.CharField(max_length=50,default='')
    village = models.CharField(max_length=50,default='')
    survey_number = models.IntegerField(max_length=50,default=0)
    total_land = models.CharField(max_length=50,default='')
    bank_loan = models.CharField(max_length=50,default='')
    bank_name = models.CharField(max_length=50,default='')
    account_number = models.IntegerField(max_length=50,default='')
    required_document_for_submission = models.FileField(null=True)    

class Apply_Pradhan_Manthri_Kisan(models.Model):
    uid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    name_of_krishibhavan = models.CharField(max_length=50,default='')
    block = models.CharField(max_length=50,default='') 
    district = models.CharField(max_length=50,default='')
    village = models.CharField(max_length=50,default='')
    fathers_name = models.CharField(max_length=50,default='')
    post_office = models.CharField(max_length=50,default='')
    pin_code = models.IntegerField(max_length=50,default=0)
    category = models.CharField(max_length=50,default='')
    date_of_birth = models.DateField(max_length=150,default='')
    ration_card_number = models.IntegerField(max_length=50,default=0)
    bank_account_number = models.IntegerField(max_length=50,default=0)
    bank_name = models.CharField(max_length=50,default='')
    branch_name = models.CharField(max_length=50,default='')
    IFSC_code = models.CharField(max_length=50,default='')
    survey_number = models.IntegerField(max_length=50,default=0)
    land_area = models.CharField(max_length=50,default='')
    ward_name = models.CharField(max_length=50,default='')
    thaluk = models.CharField(max_length=50,default='')
    required_document_for_submission = models.FileField(null=True)        

class query(models.Model):
    uid = models.ForeignKey(Register,on_delete=models.CASCADE,related_name="+",null=True)
    oid = models.ForeignKey(Register,on_delete=models.CASCADE,related_name="+",null=True)
    description = models.CharField(max_length=200,default='')
    image =  models.FileField(null=True)
    response =  models.CharField(max_length=200,default='')
    
class product_booking(models.Model):
    uid = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)  
    pid = models.ForeignKey(Products,on_delete=models.CASCADE,null=True)  
    date = models.DateField(max_length=150,default='')   
    quantity = models.CharField(max_length=150,default='') 
    amount = models.CharField(max_length=150,default='')
    

   
    





   







    










