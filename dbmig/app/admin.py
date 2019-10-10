from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Userdetails, Couriermaster, Companywarehousemaster, Usercategory, Lrdocument, Lrgeneratingmtbl

admin.site.register(Couriermaster)
admin.site.register(Companywarehousemaster)
admin.site.register(Lrdocument)
admin.site.register(Lrgeneratingmtbl)
admin.site.register(Usercategory)
# admin.site.register(Userdetails)

class UserAdmin(UserAdmin):
   add_form = UserCreationForm
   form = UserChangeForm
   model = Userdetails
   list_display = [
       'username',
       'password',
   ]
   admin.site.register(Userdetails, UserAdmin)