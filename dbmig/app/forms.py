from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.core.validators import FileExtensionValidator
from .models import Lrgeneratingmtbl, Companywarehousemaster, Vehiclemaster
from master.models import Cosingneemaster, Routemaster
from . import models


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    # def __init__(self, *args, **kwargs):
    #     super(UserForm, self).__init__(*args, **kwargs)
    #     try:
    #         self.fields['usrd_assinedwhm'].initial = self.instance.user.usrd_assinedwhm
    #     except User.DoesNotExist:
    #         pass
    class Meta:
        model = User
        fields = '__all__'

class FormUploadFileData(forms.Form):
    excel_file = forms.FileField(label='Excel File',required=False,validators=[FileExtensionValidator(['xlxs'])])
# class ProfileForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=256)
#     last_name = forms.CharField(max_length=256)

#     def __init__(self, *args, **kwargs):
#         super(ProfileForm, self).__init__(*args, **kwargs)
#         try:
#             self.fields['first_name'].initial = self.instance.user.first_name
#             self.fields['last_name'].initial = self.instance.user.last_name
#             self.fields['usrd_assinedwhm'].initial = self.instance.user.usrd_assinedwhm
#         except User.DoesNotExist:
#             pass

#     class Meta:
#          fields = ['first_name', 'last_name', 'usrd_usrcatpntr','usrd_assinedwhm','usrd_pwrd','usrd_active']


# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = User
#         fields = ['username','password']

# class ConsigneeForm(forms.ModelForm):
    
#     class Meta:
#         model : Cosingneemaster

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['consgnem_routepntr'].queryset = Routemaster.objects.none()

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

class LrgeneratingmtblForm(forms.ModelForm):
    lrg_vehcode = forms.ModelChoiceField(required=False, label='Vehicle Code', queryset=Vehiclemaster.objects.all())

    class Meta:
        model = Lrgeneratingmtbl
        fields = ('lrg_whmpntr','lrg_frttyp','lrg_vehcode')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['lrg_whmpntr'].queryset = Lrgeneratingmtbl.objects.none()
