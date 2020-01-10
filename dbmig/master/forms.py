from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Cosingneemaster, Productmaster, Productcategory, Productsubcategory, Vehiclemaster
from . import models


class CosingneemasterForm(forms.ModelForm):
    # lrg_vehcode = forms.ModelChoiceField(required=False, label='Vehicle Code', queryset=Vehiclemaster.objects.all())

    class Meta:
        model = Cosingneemaster
        fields = ('consgnem_code','consgnem_name','consgnem_branch','consgnem_address','consgnem_city','consgnem_district','consgnem_pincode','consgnem_routtyp','consgnem_gsttin','consgnem_pan','consgnem_distance','consgnem_active')

# class ConsigneeForm(forms.ModelForm):
    
#     class Meta:
#         model = Cosingneemaster 
#         fields = '__all__'


class ProductmasterForm(forms.ModelForm):
    
    class Meta:
        model = Productmaster 
        fields = '__all__'
    
class ProductcategoryForm(forms.ModelForm):
    
    class Meta:
        model = Productcategory
        fields = '__all__'

class ProductsubcategoryForm(forms.ModelForm):
    
    class Meta:
        model = Productsubcategory 
        fields = '__all__'

class VehicleForm(forms.ModelForm):

    class Meta:
        model = Vehiclemaster
        fields =('vehmas_code','vehmas_frtyppntr','vehmas_catpntr','vehmas_drivername','vehmas_phone','vehmas_desc','vehmas_active')
