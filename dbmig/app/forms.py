from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.validators import FileExtensionValidator
from .models import Lrgeneratingmtbl, Companywarehousemaster, Vehiclemaster, Lrtransation, Lrdocument, Vehiclecategory
from master.models import Cosingneemaster, Routemaster, Cosingnormaster
from . import models
from app.models import Userdetails
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#     # def __init__(self, *args, **kwargs):
#     #     super(UserForm, self).__init__(*args, **kwargs)
#     #     try:
#     #         self.fields['usrd_assinedwhm'].initial = self.instance.user.usrd_assinedwhm
#     #     except User.DoesNotExist:
#     #         pass
#     class Meta:
#         model = User
#         fields = ('username','first_name','password')

class UserdetailsCreationForm(UserCreationForm):

    class Meta:
        model = Userdetails
        fields = ('usrd_name','usrd_assinedwhm','usrd_active','usrd_usrcatpntr','username')

class UserdetailsChangeForm(UserChangeForm):

    class Meta:
        model = Userdetails
        fields = ('usrd_name', 'password','usrd_assinedwhm','usrd_usrcatpntr','usrd_active')

class FormUploadFileData(forms.Form):
    excel_file = forms.FileField(label='Excel File',required=False,validators=[FileExtensionValidator(['xlxs'])])

# class LoginForm(forms.Form): 
#     username = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)

#     def clean(self):
#         cleaned_data = super().clean()
#         username = self.cleaned_data['username']
#         password = self.cleaned_data['password']
#         user = authenticate(username=username, password=password)
#         if user is None:
#             raise forms.ValidationError('Wrong password or login')
#         else: 
#             self.user = user
#         return cleaned_data
class CompanywarehouseForm(forms.ModelForm):

    class Meta:
        model = Companywarehousemaster
        fields = ('com_wmasname','com_wmasdesc','com_wmasaddress','com_wmasactive','com_wmasremarks')


# class LrgeneratingmtblForm(forms.ModelForm):
#     lrg_vehcode = forms.ModelChoiceField(required=False, label='Vehicle Code', queryset=Vehiclemaster.objects.all())
#     class Meta:
#         model = Lrgeneratingmtbl
#         fields = ('lrg_whmpntr','lrg_frttyp','lrg_vehcode')

class LrtransationForm(forms.ModelForm):

    # lrtran_vehcatpntr = forms.ModelChoiceField(required=False, label='Vehicle Type',queryset=Vehiclemaster.objects.all())
    # lrtran_consgnrpntr = forms.ModelChoiceField(required=False,label = 'Consignor',queryset=Cosingnormaster.objects.all())
    lrtran_vehcatpntr = forms.ModelChoiceField(required=False,label = 'Vehicle Type',queryset=Vehiclecategory.objects.all(), widget= forms.Select(attrs={"onChange":'refresh()'}))

    class Meta:
        model = Lrtransation
        fields = ('lrtran_whmpntr','lrtran_frtyppntr','lrtran_vehmaspntr','lrtran_vehcatpntr','lrtran_driverdtls','lrtran_frtypebillno')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['lrtran_vehmaspntr'].widget = forms.TextInput()

# class LrdocumentForm(forms.ModelForm):

#     class Meta:
#         model = Lrdocument
#         fields = ('lrdoc_data','lrdoc_remarks')


