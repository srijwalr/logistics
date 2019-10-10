from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models


class Couriermaster(models.Model):
    # id = models.AutoField(primary_key=True)
    courmas_code = models.CharField(max_length=50, blank=True, null=True)
    courmas_desc = models.CharField(max_length=100, blank=True, null=True)
    courmas_slno = models.IntegerField(blank=True, null=True)
    courmas_active = models.CharField(max_length=1, blank=True, null=True)
    courmas_remarks = models.CharField(max_length=250, blank=True, null=True)
    courmas_makerid = models.IntegerField(blank=True, null=True)
    courmas_maketime = models.DateTimeField(blank=True, null=True)
    courmas_clntcode = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     db_table = 'couriermaster'

class Companywarehousemaster(models.Model):
    # id = models.AutoField(primary_key=True)
    com_wmasdesc = models.CharField(max_length=50, blank=True, null=True)
    com_wmasname = models.CharField(max_length=150, blank=True, null=True)
    com_wmasaddress = models.TextField(blank=True, null=True)
    com_wmascity = models.CharField(max_length=50, blank=True, null=True)
    com_wmaspincode = models.IntegerField(blank=True, null=True)
    com_wmasphone = models.IntegerField(blank=True, null=True)
    com_wmascommaspntr = models.IntegerField(blank=True, null=True)
    com_wmascomzmaspntr = models.IntegerField(blank=True, null=True)
    com_wmas_clntmaspntr = models.ForeignKey(Couriermaster,null = True, blank = True, on_delete = models.CASCADE)
    com_wmasslno = models.IntegerField(blank=True, null=True)
    com_wmasremarks = models.CharField(max_length=250, blank=True, null=True)
    com_wmasactive = models.CharField(max_length=2, blank=True, null=True)
    com_wmas_accwmas = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     db_table = 'companywarehousemaster'

class Usercategory(models.Model):
    # id = models.BigIntegerField(primary_key=True)
    usrcat_code = models.CharField(max_length=4, blank=True, null=True)
    usercat_desc = models.CharField(max_length=20, blank=True, null=True)
    usercat_slno = models.IntegerField(blank=True, null=True)
    usercat_remarks = models.CharField(max_length=250, blank=True, null=True)
    usercat_active = models.CharField(max_length=1, blank=True, null=True)

    # class Meta:
    #     db_table = 'usercategory'

class Userdetails(AbstractUser):
    # id = models.AutoField(primary_key = True)
    usrd_usrcatpntr = models.ForeignKey(Usercategory,null = True, blank = True, on_delete = models.CASCADE)
    usrd_code = models.IntegerField(blank=True, null=True)
    usrd_assinedwhm = models.ForeignKey(Companywarehousemaster, null = True, blank = True, on_delete = models.CASCADE)
    usrd_name = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=256, blank=True, null=True)
    usrd_slno = models.IntegerField(blank=True, null=True)
    usrd_remarks = models.CharField(max_length=250, blank=True, null=True)
    usrd_active = models.CharField(max_length=1, blank=True, null=True)
    usrd_makerid = models.IntegerField(blank=True, null=True)
    usrd_maketime = models.DateTimeField(blank=True, null=True)
    usrd_logcount = models.IntegerField(blank=True, null=True)
    usrd_logattempt = models.IntegerField(blank=True, null=True)
    

    # class Meta:
    #     db_table = 'userdetails'

    # def __str__(self):
    #     return self.usrd_name


class Vehiclemaster(models.Model):
    # vehmas_id = models.AutoField(primary_key=True)
    vehmas_code = models.CharField(max_length=50, primary_key=True)
    vehmas_desc = models.CharField(max_length=100, blank=True, null=True)
    vehmas_catpntr = models.IntegerField(blank=True, null=True)
    vehmas_frtyppntr = models.IntegerField(blank=True, null=True)
    vehmas_modepntr = models.IntegerField(blank=True, null=True)
    vehmas_slno = models.IntegerField(blank=True, null=True)
    vehmas_active = models.CharField(max_length=1, blank=True, null=True)
    vehmas_remarks = models.CharField(max_length=250, blank=True, null=True)
    vehmas_makerid = models.IntegerField(blank=True, null=True)
    vehmas_maketime = models.DateTimeField(blank=True, null=True)
    vehmas_clntpntr = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'vehiclemaster'


class Lrgeneratingmtbl(models.Model):
    # lrg_id = models.IntegerField( blank=True, null=True)
    lrg_whmpntr = models.ForeignKey(Companywarehousemaster,verbose_name='Consignor', blank = True, null = True, on_delete = models.CASCADE)
    lrg_tpcode = models.TextField(blank=True, null=True)
    lrg_shiptocode = models.TextField(blank=True, null=True)
    lrg_pl = models.TextField(blank=True, null=True)
    lrg_div = models.TextField(blank=True, null=True)
    lrg_matgrp = models.TextField(blank=True, null=True)
    lrg_material = models.TextField(blank=True, null=True)
    lrg_hsncode = models.TextField(blank=True, null=True)
    lrg_taxinvno = models.TextField(blank=True, null=True)
    lrg_intinvno = models.TextField(blank=True, null=True)
    lrg_date = models.DateField(blank=True, null=True)
    lrg_qty = models.IntegerField(blank=True, null=True)
    lrg_frttyp = models.IntegerField('Freight Type', blank=True, null=True)
    lrg_vehcode = models.TextField('Vehicle Code', blank=True, null=True)
    lrg_unloadchrg = models.FloatField(blank=True, null=True)
    lrg_unloadchremrks = models.TextField(blank=True, null=True)
    lrg_courierid = models.IntegerField(blank=True, null=True)
    lrg_courifrghchrg = models.FloatField(blank=True, null=True)
    lrg_couriaddchrg = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    lrg_frghtchrgremrks = models.TextField(blank=True, null=True)
    lrg_addchrgremarks = models.TextField(blank=True, null=True)
    # lrg_terminal = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     db_table = 'lrgeneratingmtbl'

class Lrdocument(models.Model):
    # lrdoc_id = models.IntegerField( blank=True, null=True)
    lrdoc_lrno = models.CharField(max_length=50, blank=True, null=True)
    lrdoc_name = models.CharField(max_length=50, blank=True, null=True)
    lrdoc_ctype = models.CharField(max_length=200, blank=True, null=True)
    lrdoc_data = models.BinaryField(blank=True, null=True)
    lrdoc_remarks = models.TextField(blank=True, null=True)
    lrdoc_whmcode = models.IntegerField(blank=True, null=True)
    lrdoc_makingtime = models.DateTimeField(blank=True, null=True)
    lrdoc_makerid = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'lrdocument'

