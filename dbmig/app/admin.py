from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import UserdetailsCreationForm, UserdetailsChangeForm
from .models import Userdetails, Couriermaster, Companywarehousemaster, Usercategory, Lrdocument, Lrgeneratingmtbl, Lrtransation, Lrtranslink, Lraccountcharges, Lrtransactionaccount, LogLrtransation, LogLrtranslink

admin.site.register(Couriermaster)
admin.site.register(Companywarehousemaster)
admin.site.register(Lrdocument)
admin.site.register(Lrgeneratingmtbl)
admin.site.register(Lrtransation)
admin.site.register(Lrtranslink)
admin.site.register(Usercategory)
admin.site.register(Lraccountcharges)
admin.site.register(Lrtransactionaccount)
admin.site.register(LogLrtranslink)
admin.site.register(LogLrtransation)
# admin.site.register(Userdetails)

class CustomUserAdmin(UserAdmin):
   add_form = UserdetailsCreationForm   
   form = UserdetailsChangeForm
   model = Userdetails
   list_display = [
       'username',
       'password',
   ]
   fieldsets = UserAdmin.fieldsets + (
      ('Standard info', {
          'fields': ('usrd_name','usrd_assinedwhm','usrd_usrcatpntr','usrd_active')
      }),
   )

admin.site.register(Userdetails, CustomUserAdmin)