from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import Cosingneemaster, Productmaster, Productcategory, Productsubcategory
from . import models


class CosingneemasterForm(forms.ModelForm):
    # lrg_vehcode = forms.ModelChoiceField(required=False, label='Vehicle Code', queryset=Vehiclemaster.objects.all())

    class Meta:
        model = Cosingneemaster
        fields = '__all__'
        # fields = ('lrg_whmpntr','lrg_frttyp','lrg_vehcode')

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