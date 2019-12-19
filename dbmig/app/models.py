from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser
from django.db import models
from master.models import Cosingneemaster, Productsubcategory, Productmaster, Productcategory, Freighttypes, Vehiclecategory, Vehiclemaster, Cosingnormaster
from django.dispatch import receiver
from django.db.models.signals import pre_delete
from django.forms.models import model_to_dict
from django.utils.timezone import now



class Returnlrtranslink(models.Model):
    # retrn_id = models.AutoField(primary_key=True)
    retrn_waybillpntr = models.CharField(max_length=150, blank=True, null=True)
    retrn_consignepntr = models.IntegerField(blank=True, null=True)
    retrn_proscatpntr = models.IntegerField(blank=True, null=True)
    retrn_quantity = models.IntegerField(blank=True, null=True)
    retrn_authorize = models.CharField(max_length=1, blank=True, null=True)
    retrn_maketime = models.DateTimeField(blank=True, null=True)
    retrn_makerid = models.IntegerField(blank=True, null=True)
    retrn_whmcode = models.IntegerField(blank=True, null=True)
    retrn_clntcode = models.IntegerField(blank=True, null=True)
    retrn_tripno = models.CharField(max_length=150, blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'returnlrtranslink'


class LogAraTransaction(models.Model):
    # log_ara_id = models.AutoField()
    log_ara_waybillno = models.CharField(max_length=100, blank=True, null=True)
    log_ara_arano = models.CharField(max_length=100, blank=True, null=True)
    log_ara_oldmatcode = models.CharField(max_length=100, blank=True, null=True)
    log_ara_newmatcode = models.CharField(max_length=100, blank=True, null=True)
    log_ara_quatity = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    log_ara_trandate = models.DateField(blank=True, null=True)
    log_ara_docdate = models.CharField(max_length=10, blank=True, null=True)
    log_ara_issuedate = models.CharField(max_length=10, blank=True, null=True)
    log_ara_consgnrpntr = models.IntegerField(blank=True, null=True)
    log_ara_customername = models.CharField(max_length=50, blank=True, null=True)
    log_ara_cutomeraddress = models.TextField(blank=True, null=True)
    log_ara_cutomercity = models.CharField(max_length=100, blank=True, null=True)
    log_ara_frieghttyp = models.IntegerField(blank=True, null=True)
    log_ara_saletypepntr = models.IntegerField(blank=True, null=True)
    log_ara_vehpntr = models.IntegerField(blank=True, null=True)
    log_ara_courmaspntr = models.IntegerField(blank=True, null=True)
    log_ara_courdockchrg = models.FloatField(blank=True, null=True)
    log_ara_frieghtchrg = models.FloatField(blank=True, null=True)
    log_ara_whmpntr = models.IntegerField(blank=True, null=True)
    log_ara_authorise = models.CharField(max_length=1, blank=True, null=True)
    log_ara_slno = models.IntegerField(blank=True, null=True)
    log_ara_active = models.CharField(max_length=1, blank=True, null=True)
    log_ara_closeddate = models.DateField(blank=True, null=True)
    log_ara_makerid = models.IntegerField(blank=True, null=True)
    log_ara_maketime = models.DateTimeField(blank=True, null=True)
    log_ara_tripstatus = models.CharField(max_length=1, blank=True, null=True)
    log_ara_tripcloseddate = models.DateField(blank=True, null=True)
    log_ara_frtypebillno = models.CharField(max_length=20, blank=True, null=True)
    log_ara_closeid = models.IntegerField(blank=True, null=True)
    log_ara_tripclaimno = models.CharField(max_length=150, blank=True, null=True)
    log_ara_canceldate = models.DateTimeField(blank=True, null=True)
    log_ara_cancelid = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'log_ara_transaction'



class AraTransaction(models.Model):
    # ara_id = models.AutoField()
    ara_waybillno = models.CharField(max_length=100, blank=True, null=True)
    ara_arano = models.CharField(max_length=100, blank=True, null=True)
    ara_oldmatcode = models.CharField(max_length=100, blank=True, null=True)
    ara_newmatcode = models.CharField(max_length=100, blank=True, null=True)
    ara_quatity = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    ara_trandate = models.DateField(blank=True, null=True)
    ara_docdate = models.CharField(max_length=10, blank=True, null=True)
    ara_issuedate = models.CharField(max_length=10, blank=True, null=True)
    ara_consgnrpntr = models.IntegerField(blank=True, null=True)
    ara_customername = models.CharField(max_length=50, blank=True, null=True)
    ara_cutomeraddress = models.TextField(blank=True, null=True)
    ara_cutomercity = models.CharField(max_length=100, blank=True, null=True)
    ara_frieghttyp = models.IntegerField(blank=True, null=True)
    ara_saletypepntr = models.IntegerField(blank=True, null=True)
    ara_vehpntr = models.IntegerField(blank=True, null=True)
    ara_courmaspntr = models.IntegerField(blank=True, null=True)
    ara_courdockchrg = models.FloatField(blank=True, null=True)
    ara_frieghtchrg = models.FloatField(blank=True, null=True)
    ara_whmpntr = models.IntegerField(blank=True, null=True)
    ara_authorise = models.CharField(max_length=1, blank=True, null=True)
    ara_slno = models.IntegerField(blank=True, null=True)
    ara_active = models.CharField(max_length=1, blank=True, null=True)
    ara_closeddate = models.DateField(blank=True, null=True)
    ara_makerid = models.IntegerField(blank=True, null=True)
    ara_maketime = models.DateTimeField(blank=True, null=True)
    ara_tripstatus = models.CharField(max_length=1, blank=True, null=True)
    ara_tripcloseddate = models.DateField(blank=True, null=True)
    ara_frtypebillno = models.CharField(max_length=20, blank=True, null=True)
    ara_closeid = models.IntegerField(blank=True, null=True)
    ara_tripclaimno = models.CharField(max_length=150, blank=True, null=True)
    ara_driverdtls = models.CharField(max_length=150, blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'ara_transaction'


class Aralrgenratingtbl(models.Model):
    arano = models.CharField(max_length=100, blank=True, null=True)
    docdate = models.DateField(blank=True, null=True)
    rettpye = models.CharField(max_length=10, blank=True, null=True)
    plant = models.CharField(max_length=10, blank=True, null=True)
    inspdate = models.DateField(blank=True, null=True)
    custname = models.CharField(max_length=100, blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)
    oldmaterial = models.CharField(max_length=100, blank=True, null=True)
    oldmodelhsncode = models.CharField(max_length=100, blank=True, null=True)
    newmaterial = models.CharField(max_length=100, blank=True, null=True)
    newmodelhsncode = models.CharField(max_length=100, blank=True, null=True)
    bsmstatus = models.CharField(max_length=50, blank=True, null=True)
    approvaldate = models.DateField(blank=True, null=True)
    issuematerial = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    issueddate = models.DateField(blank=True, null=True)
    issuedmaterialslno = models.CharField(max_length=150, blank=True, null=True)
    qty = models.IntegerField(blank=True, null=True)
    frttyp = models.IntegerField(blank=True, null=True)
    vehcode = models.CharField(max_length=50, blank=True, null=True)
    unloadchrg = models.FloatField(blank=True, null=True)
    unloadchremrks = models.CharField(max_length=500, blank=True, null=True)
    courierid = models.IntegerField(blank=True, null=True)
    courifrghchrg = models.FloatField(blank=True, null=True)
    couriaddchrg = models.FloatField(blank=True, null=True)
    frghtchrgremrks = models.CharField(max_length=500, blank=True, null=True)
    addchrgremarks = models.CharField(max_length=500, blank=True, null=True)
    terminal = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'aralrgenratingtbl'

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

class Companyzonemaster(models.Model):
    # com_zmasid = models.AutoField(primary_key=True)
    com_zmasdesc = models.CharField(max_length=50, blank=True, null=True)
    com_zmasname = models.CharField(max_length=50, blank=True, null=True)
    com_zmascommaspntr = models.IntegerField(blank=True, null=True)
    com_zmasslno = models.IntegerField(blank=True, null=True)
    com_zmasremarks = models.CharField(max_length=250, blank=True, null=True)
    com_zmasactive = models.CharField(max_length=2, blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'companyzonemaster'

class Companywarehousemaster(models.Model):
    # id = models.AutoField(primary_key=True)
    com_wmasdesc = models.CharField(max_length=50, verbose_name = 'Description', blank=True, null=True)
    com_wmasname = models.CharField(max_length=150, verbose_name = 'Name', blank=True, null=True)
    com_wmasaddress = models.CharField( max_length = 200, verbose_name = 'Address', blank=True, null=True)
    com_wmascity = models.CharField( verbose_name = 'City',max_length=50, blank=True, null=True)
    com_wmaspincode = models.IntegerField( verbose_name = 'PIN', blank=True, null=True)
    com_wmasphone = models.IntegerField(verbose_name = 'Phone', blank=True, null=True)
    com_wmascommaspntr = models.IntegerField( blank=True, null=True)
    com_wmascomzmaspntr = models.ForeignKey(Companyzonemaster, verbose_name = 'Zone', blank=True, null=True, on_delete = models.CASCADE)
    com_wmas_clntmaspntr = models.ForeignKey(Couriermaster, null = True, blank = True, on_delete = models.CASCADE)
    com_wmasslno = models.IntegerField(verbose_name = 'Serial no.', blank=True, null=True)
    com_wmasremarks = models.TextField(verbose_name = 'Remarks', blank=True, null=True)
    com_wmasactive = models.CharField(verbose_name = 'Status', max_length=10, blank=True, null=True)
    com_wmas_accwmas = models.IntegerField(blank=True, null=True)
    
    def __str__(self):
        return str(self.com_wmasname)
    # class Meta:
    #     db_table = 'companywarehousemaster'

class UserBranchChangeMTbl(models.Model):
    user_name = models.CharField(max_length=15)
    user_current_brcode = models.CharField(max_length=5)
    user_new_brcode = models.CharField(max_length=5)
    modification_reason = models.CharField(max_length=100)
    user_modifieduser = models.CharField(max_length=50)
    user_modifiedtime = models.DateTimeField()
    sl_no = models.IntegerField()

    # class Meta:
    #     managed = False
    #     db_table = 'user_branch_change_m_tbl'


class Usercategory(models.Model):
    # id = models.BigIntegerField(primary_key=True)
    usrcat_code = models.CharField(max_length=4, blank=True, null=True)
    usercat_desc = models.CharField(max_length=20, blank=True, null=True)
    usercat_slno = models.IntegerField(blank=True, null=True)
    usercat_remarks = models.CharField(max_length=250, blank=True, null=True)
    usercat_active = models.CharField(max_length=1, blank=True, null=True)

    def __str__(self):
        return str(self.usercat_desc)
    # class Meta:
    #     db_table = 'usercategory'

class Userdetails(AbstractUser): 
    # id = models.AutoField(primary_key = True)
    usrd_usrcatpntr = models.ForeignKey(Usercategory,null = True, blank = True, verbose_name= 'User Type', on_delete = models.CASCADE)
    usrd_code = models.IntegerField(blank=True, null=True)
    usrd_assinedwhm = models.ForeignKey(Companywarehousemaster, verbose_name= 'Assigned Warehouse', null = True, blank = True, on_delete = models.CASCADE)
    usrd_name = models.CharField(max_length=50, verbose_name='Employee name', unique=True, blank=True, null=True)
    password = models.CharField(max_length=256, blank=True, null=True)
    usrd_slno = models.IntegerField(blank=True, null=True)
    usrd_remarks = models.CharField(max_length=250, blank=True, null=True)
    usrd_active = models.CharField(max_length=1, verbose_name='User Status', blank=True, null=True)
    usrd_makerid = models.IntegerField(blank=True, null=True)
    usrd_maketime = models.DateTimeField(blank=True, null=True)
    usrd_logcount = models.IntegerField(blank=True, null=True)
    usrd_logattempt = models.IntegerField(blank=True, null=True)
    
    # USERNAME_FIELD = 'usrd_name'
    # class Meta:
    #     db_table = 'userdetails'

    def __str__(self):
        return str(self.usrd_name)


# class Vehiclemaster(models.Model):
#     # vehmas_id = models.AutoField(primary_key=True)
#     vehmas_code = models.CharField(max_length=50, primary_key=True)
#     vehmas_desc = models.CharField(max_length=100, blank=True, null=True)
#     vehmas_catpntr = models.IntegerField(blank=True, null=True)
#     vehmas_frtyppntr = models.IntegerField(blank=True, null=True)
#     vehmas_modepntr = models.IntegerField(blank=True, null=True)
#     vehmas_slno = models.IntegerField(blank=True, null=True)
#     vehmas_active = models.CharField(max_length=1, blank=True, null=True)
#     vehmas_remarks = models.CharField(max_length=250, blank=True, null=True)
#     vehmas_makerid = models.IntegerField(blank=True, null=True)
#     vehmas_maketime = models.DateTimeField(blank=True, null=True)
#     vehmas_clntpntr = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'vehiclemaster'


class UnloadchargesettingsPTbl(models.Model):
    # unloadc_id = models.AutoField(primary_key=True)
    unloadc_consgnepntr = models.IntegerField(blank=True, null=True)
    unloadc_whmcode = models.IntegerField(blank=True, null=True)
    unloadc_materialpntr = models.IntegerField(blank=True, null=True)
    unloadc_effectivedate = models.DateTimeField(blank=True, null=True)
    unloadc_circulardate = models.DateTimeField(blank=True, null=True)
    unloadc_circularno = models.CharField(max_length=15, blank=True, null=True)
    unloadc_charge = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    unloadc_rmrks = models.TextField(blank=True, null=True)
    unloadc_status = models.CharField(max_length=1, blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'unloadchargesettings_p_tbl'

class Lrgeneratingmtbl(models.Model):
    # lrg_id = models.IntegerField( blank=True, null=True)
    lrg_whmpntr = models.ForeignKey(Companywarehousemaster,verbose_name='Consignor', blank = True, null = True, on_delete = models.CASCADE)
    lrg_tpcode = models.TextField(blank=True, null=True)
    lrg_shiptocode = models.CharField(max_length=15, blank=True, null=True)
    lrg_pl = models.TextField(blank=True, null=True)
    lrg_div = models.CharField(max_length=10, blank=True, null=True)
    lrg_matgrp = models.TextField(blank=True, null=True)
    lrg_material = models.CharField(max_length=15, blank=True, null=True)
    lrg_hsncode = models.CharField(max_length=15, blank=True, null=True)
    lrg_taxinvno = models.CharField(max_length = 12, blank=True, null=True)
    lrg_intinvno = models.CharField(max_length = 10, blank=True, null=True)
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

#     def save(self, *args, **kwargs):
#         try:
#             voucher_type = VoucherTypeMaster.objects.get(
#                 company=self.company,
#                 code=self.type.code
#                 )
#             voucher_type.last_number += 1
#             voucher_type.save()   
#             self.number = voucher_type.last_number
#             self.type.save() # throws exception
#         except Exception,e:


    # def save(self, *args, **kwargs):     
    #     print(self.request)
    #     a = Cosingneemaster.objects.get(id = id)
    #     a.consgnem_code = self.lrg_shiptocode
    
    #     super(Lrgeneratingmtbl, self).save(*args, **kwargs)

    class Meta:
        unique_together = ('lrg_shiptocode','lrg_material','lrg_intinvno')
    #     db_table = 'lrgeneratingmtbl' 

class Lrdocument(models.Model):
    # lrdoc_id = models.IntegerField( blank=True, null=True)
    lrdoc_lrno = models.CharField(max_length=50, blank=True, null=True)
    lrdoc_name = models.CharField(max_length=50, blank=True, null=True)
    lrdoc_ctype = models.CharField(max_length=200, blank=True, null=True)
    lrdoc_data = models.FileField(blank=True, null=True, verbose_name='File')
    lrdoc_remarks = models.CharField(blank=True, max_length = 50,null=True, verbose_name='Remarks')
    lrdoc_whmcode = models.IntegerField(blank=True, null=True)
    lrdoc_makingtime = models.DateTimeField(blank=True, null=True)
    lrdoc_makerid = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     db_table = 'lrdocument'


class LogLrtransation(models.Model):
    # log_lrtran_id = models.AutoField()
    log_lrtran_waybillno = models.CharField(max_length=50, blank=True, null=True)
    log_lrtran_invdate = models.CharField(max_length=10, blank=True, null=True)
    log_lrtran_date = models.DateField(blank=True, null=True)
    log_lrtran_consgnrpntr = models.IntegerField(blank=True, null=True)
    log_lrtran_consgnepntr = models.IntegerField(blank=True, null=True)
    log_lrtran_invidpntr = models.IntegerField(blank=True, null=True)
    log_lrtran_frtyppntr = models.CharField(max_length = 20, blank=True, null=True)
    log_lrtran_km = models.FloatField(blank=True, null=True)
    log_lrtran_kmrate = models.FloatField(blank=True, null=True)
    log_lrtran_vehcatpntr = models.CharField(max_length = 20, blank=True, null=True)
    log_lrtran_vehmaspntr = models.CharField(max_length = 20, blank=True, null=True)
    log_lrtran_courmaspntr = models.IntegerField(blank=True, null=True)
    log_lrtran_courcatpntr = models.IntegerField(blank=True, null=True)
    log_lrtran_courdockchrg = models.FloatField(blank=True, null=True)
    log_lrtran_courcharge = models.FloatField(blank=True, null=True)
    log_lrtran_courchargenarration = models.CharField(max_length=300, blank=True, null=True)
    log_lrtran_coutaddcharge = models.FloatField(blank=True, null=True)
    log_lrtran_coutaddchargenarration = models.CharField(max_length=300, blank=True, null=True)
    log_lrtran_whmpntr = models.CharField(max_length = 30, null=True)
    log_lrtran_authorise = models.CharField(max_length=1, blank=True, null=True)
    log_lrtran_slno = models.IntegerField(blank=True, null=True)
    log_lrtran_active = models.CharField(max_length=1, blank=True, null=True)
    log_lrtran_closeddate = models.DateField(blank=True, null=True)
    log_lrtran_remarks = models.CharField(max_length=300, blank=True, null=True)
    log_lrtran_makerid = models.IntegerField(blank=True, null=True)
    log_lrtran_maketime = models.DateTimeField(blank=True, null=True)
    log_lrtran_frtypebillno = models.CharField(max_length=20, blank=True, null=True)
    log_lrtran_tripstatus = models.CharField(max_length=1, blank=True, null=True)
    log_lrtran_tripclosedate = models.DateField(blank=True, null=True)
    log_lrtran_tripcloseuid = models.IntegerField(blank=True, null=True)
    log_lrtran_tripclaimno = models.CharField(max_length=150, blank=True, null=True)
    log_lrtran_canceltime = models.DateTimeField(default = now,blank =True, null=True)
    log_lrtran_cancelid = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'log_lrtransation'


class LogLrtranslink(models.Model):
    # log_trans_id = models.AutoField()
    log_trans_waybillpntr = models.CharField(max_length=50, blank=True, null=True)
    log_trans_whmpntr = models.IntegerField(blank=True, null=True)
    log_trans_invnumber = models.TextField(blank=True, null=True)
    log_trans_productpntr = models.IntegerField(blank=True, null=True)
    log_trans_consgnepntr = models.IntegerField(blank=True, null=True)
    log_trans_qunatity = models.IntegerField(blank=True, null=True)
    log_trans_authorize = models.CharField(max_length=1, blank=True, null=True)
    log_trans_maketime = models.CharField(max_length=12, blank=True, null=True)
    log_trans_makerid = models.IntegerField(blank=True, null=True)
    log_trans_canceltime = models.DateTimeField(blank=True, null=True)
    log_trans_cancelid = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'log_lrtranslink'



class Lrtransation(models.Model):   
    lrtran_waybillno = models.CharField(max_length=50, blank=True, null=True)
    lrtran_invdate = models.CharField(max_length=10, blank=True, null=True)
    lrtran_date = models.DateField(blank=True, null=True)
    lrtran_consgnrpntr = models.ForeignKey(Cosingnormaster,verbose_name='Consignor', blank = True, null = True, on_delete = models.CASCADE)
    lrtran_consgnepntr = models.ForeignKey(Cosingneemaster ,verbose_name='Consignee', blank = True, null = True, on_delete = models.CASCADE)
    lrtran_invidpntr = models.IntegerField(blank=True, null=True)
    lrtran_frtyppntr = models.ForeignKey(Freighttypes ,verbose_name='Freight Type', blank = True, null = True, on_delete = models.CASCADE)
    lrtran_km = models.FloatField(blank=True, null=True)
    lrtran_kmrate = models.FloatField(blank=True, null=True)
    lrtran_vehcatpntr = models.ForeignKey(Vehiclecategory,verbose_name='Vehicle Category', blank = True, null = True, on_delete = models.CASCADE)
    lrtran_vehmaspntr = models.ForeignKey(Vehiclemaster,verbose_name='Vehicle', blank = True, null = True, on_delete = models.CASCADE)
    lrtran_courmaspntr = models.IntegerField(blank=True, null=True)
    lrtran_courcatpntr = models.IntegerField(blank=True, null=True)
    lrtran_courdockchrg = models.FloatField(blank=True, null=True)
    lrtran_courcharge = models.FloatField(blank=True, null=True)
    lrtran_courchargenarration = models.CharField(max_length=300, blank=True, null=True)
    lrtran_coutaddcharge = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    lrtran_coutaddchargenarration = models.CharField(max_length=300, blank=True, null=True)
    lrtran_whmpntr = models.ForeignKey(Companywarehousemaster,verbose_name='Warehouse', blank = True, null = True, on_delete = models.CASCADE)
    lrtran_authorise = models.CharField(max_length=1, blank=True, null=True)
    lrtran_slno = models.IntegerField(blank=True, null=True)
    lrtran_active = models.CharField(max_length=1, blank=True, null=True)
    lrtran_closeddate = models.DateField(blank=True, null=True)
    lrtran_remarks = models.CharField(max_length=300, blank=True, null=True)
    lrtran_makerid = models.IntegerField(blank=True, null=True)
    lrtran_maketime = models.DateTimeField(blank=True, null=True)
    lrtran_frtypebillno = models.CharField(max_length=20, blank=True, null=True, verbose_name='Trip Number')
    lrtran_tripstatus = models.CharField(max_length=1, blank=True, null=True)
    lrtran_tripclosedate = models.DateTimeField(blank=True, null=True)
    lrtran_tripcloseuid = models.IntegerField(blank=True, null=True)
    lrtran_tripclaimno = models.CharField(max_length=150, blank=True, null=True)
    lrtran_driverdtls = models.CharField(max_length=150, blank=True, null=True, verbose_name='Driver Name')
    lrtran_driverphone = models.CharField(max_length= 25, blank = True, null= True)
    
    # def backup_data(sender, **kwargs):
    #     instance = Lrtransation.objects.get(slug = 'id')

    #     kwargs = model_to_dict(instance, exclude=['lrtran_driverdtls'])
    #     new_instance = LogLrtransation.objects.create(**kwargs)
    
    # pre_delete.connect(backup_data, sender=LogLrtransation)
    
@receiver(pre_delete, sender=Lrtransation)
def _pre_delete_receiver(sender, instance, **kwargs):
    # instance = Lrtransation.objects.get(id = 'id')
    # kwargs = model_to_dict(instance, exclude=['id','lrtran_driverdtls'])

    new_instance = LogLrtransation()

    new_instance.log_lrtran_waybillno = instance.lrtran_waybillno
    new_instance.log_lrtran_invdate = instance.lrtran_invdate
    new_instance.log_lrtran_date = instance.lrtran_date
    new_instance.log_lrtran_consgnrpntr = instance.lrtran_consgnrpntr
    new_instance.log_lrtran_consgnepntr = instance.lrtran_consgnepntr
    new_instance.log_lrtran_invidpntr = instance.lrtran_invidpntr
    new_instance.log_lrtran_frtyppntr = str(instance.lrtran_frtyppntr)
    new_instance.log_lrtran_km = instance.lrtran_km
    new_instance.log_lrtran_kmrate = instance.lrtran_kmrate
    new_instance.log_lrtran_vehcatpntr = str(instance.lrtran_vehcatpntr)
    new_instance.log_lrtran_vehmaspntr = str(instance.lrtran_vehmaspntr)
    new_instance.log_lrtran_courmaspntr = instance.lrtran_courmaspntr
    new_instance.log_lrtran_courcatpntr = instance.lrtran_courcatpntr
    new_instance.log_lrtran_courdockchrg = instance.lrtran_courdockchrg
    new_instance.log_lrtran_courchargenarration = instance.lrtran_courchargenarration
    new_instance.log_lrtran_coutaddchargenarration = instance.lrtran_coutaddchargenarration
    new_instance.log_lrtran_whmpntr = str(instance.lrtran_whmpntr)
    new_instance.log_lrtran_slno = instance.lrtran_slno
    new_instance.log_lrtran_active = instance.lrtran_active
    new_instance.log_lrtran_closeddate = instance.lrtran_closeddate
    new_instance.log_lrtran_remarks = instance.lrtran_remarks
    new_instance.log_lrtran_makerid = instance.lrtran_makerid
    new_instance.log_lrtran_maketime = instance.lrtran_maketime
    new_instance.log_lrtran_frtypebillno = instance.lrtran_frtypebillno
    new_instance.log_lrtran_tripstatus = instance.lrtran_tripstatus
    new_instance.log_lrtran_tripclosedate = instance.lrtran_tripclosedate
    new_instance.log_lrtran_tripcloseuid = instance.lrtran_tripcloseuid
    new_instance.log_lrtran_tripclaimno = instance.lrtran_tripclaimno
    new_instance.log_lrtran_driverdtls = instance.lrtran_driverdtls
    new_instance.log_lrtran_cancelid = instance.id

    new_instance.save()
    
        
    # class Meta:
    #     managed = False
    #     db_table = 'lrtransation'

class Lrtranslink(models.Model):
    trans_waybillpntr = models.CharField(max_length=50, blank=True, null=True)
    trans_whmpntr = models.ForeignKey(Companywarehousemaster, blank=True, null=True, on_delete = models.CASCADE)
    trans_invnumber = models.CharField(max_length=50, blank=True, null=True)
    trans_productpntr = models.ForeignKey( Productmaster, blank=True, null=True, on_delete = models.CASCADE)
    trans_consgnepntr = models.ForeignKey(Cosingneemaster, blank=True, null=True, on_delete = models.CASCADE)
    trans_qunatity = models.IntegerField(blank=True, null=True)
    trans_authorize = models.CharField(max_length=1, blank=True, null=True)
    trans_maketime = models.CharField(max_length=12, blank=True, null=True)
    trans_makerid = models.IntegerField(blank=True, null=True)

#     class Meta:
#         managed = False    

#         db_table = 'lrtranslink'


class Lrtransactionaccount(models.Model):
    lrtr_acccode = models.IntegerField()
    lrtr_accname = models.CharField(max_length=100, blank=True, null=True)
    lrtr_shortname = models.CharField(max_length=20, blank=True, null=True)
    lrtr_accgrpcode = models.IntegerField(blank = True, null = True)
    lrtr_slno = models.IntegerField(blank=True, null=True)
    lrtr_active = models.CharField(max_length=1, blank=True, null=True)
    lrtr_remarks = models.CharField(max_length=250, blank=True, null=True)
    lrtr_makingtime = models.DateTimeField(blank=True, null=True)
    lrtr_makerid = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     managed = False   
    #     db_table = 'lrtransactionaccount'


class Lraccountcharges(models.Model):
    # lra_tranid = models.AutoField(primary_key=True)
    lra_tranno = models.CharField(max_length=50, blank=True, null=True)
    lra_trandate = models.DateField(blank=True, null=True)
    lra_accid = models.DecimalField(max_digits=18, decimal_places=0, blank=True, null=True)
    lra_lrno = models.CharField(max_length=50, blank=True, null=True)
    lra_whmpntr = models.ForeignKey(Companywarehousemaster, blank=True, null=True, on_delete = models.CASCADE)
    lra_accode = models.ForeignKey(Lrtransactionaccount, blank=True, null=True, on_delete = models.CASCADE)
    lra_trantype = models.CharField(max_length=1, blank=True, null=True)
    lra_amount = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    lra_narration = models.TextField(blank=True, null=True)
    lra_authorized = models.CharField(max_length=1, blank=True, null=True)
    lra_makerid = models.IntegerField(blank=True, null=True)
    lra_maketime = models.DateTimeField(blank=True, null=True)
    lra_checkerid = models.IntegerField(blank=True, null=True)
    lra_checkingtime = models.DateTimeField(blank=True, null=True)
    lra_tripno = models.CharField(max_length=50, blank=True, null=True)
    lra_orgwhmcode = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'lraccountcharges'

class LogReturnlrtranslink(models.Model):
    # log_retrn_id = models.AutoField()
    log_retrn_waybillpntr = models.CharField(max_length=150, blank=True, null=True)
    log_retrn_consignepntr = models.IntegerField(blank=True, null=True)
    log_retrn_proscatpntr = models.IntegerField(blank=True, null=True)
    log_retrn_quantity = models.IntegerField(blank=True, null=True)
    log_retrn_authorize = models.CharField(max_length=1, blank=True, null=True)
    log_retrn_maketime = models.DateTimeField(blank=True, null=True)
    log_retrn_makerid = models.IntegerField(blank=True, null=True)
    log_retrn_whmcode = models.IntegerField(blank=True, null=True)
    log_retrn_clntcode = models.IntegerField(blank=True, null=True)
    log_retrn_tripno = models.CharField(max_length=150, blank=True, null=True)
    log_retrn_canceltime = models.DateTimeField(blank=True, null=True)
    log_retrn_cancelid = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'log_returnlrtranslink'

# class MonthTbl(models.Model):
#     # month_id = models.AutoField()
#     month_code = models.CharField(max_length=2, blank=True, null=True)
#     month_name = models.CharField(max_length=10, blank=True, null=True)
#     month_shrtname = models.CharField(max_length=5, blank=True, null=True)

#     # class Meta:
#     #     managed = False
#     #     db_table = 'month_tbl'

class MultipleconsigneRTbl(models.Model):
    # id = models.DecimalField(max_digits=18, decimal_places=0)
    lrtran_waybillno = models.TextField(blank=True, null=True)
    tran_date = models.CharField(max_length=50, blank=True, null=True)
    consgnem_name = models.TextField(blank=True, null=True)
    consgnem_address = models.TextField(blank=True, null=True)
    consgnem_district = models.TextField(blank=True, null=True)
    consgnem_routtyp = models.TextField(blank=True, null=True)
    consgnem_distance = models.FloatField(blank=True, null=True)
    consgnrm_name = models.TextField(blank=True, null=True)
    consgnrm_address = models.TextField(blank=True, null=True)
    consgnem_city = models.TextField(blank=True, null=True)
    consgnem_gsttin = models.TextField(blank=True, null=True)
    vehcat_desc = models.TextField(blank=True, null=True)
    vehmas_code = models.TextField(blank=True, null=True)
    invoiceno = models.TextField(blank=True, null=True)
    invtota = models.IntegerField(blank=True, null=True)
    invtotalwords = models.TextField(blank=True, null=True)
    qtytotal = models.IntegerField(blank=True, null=True)
    qtytotalwords = models.TextField(blank=True, null=True)
    division = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(blank=True, null=True)
    vouchermode = models.TextField(blank=True, null=True)
    frtypbillno = models.TextField(blank=True, null=True)
    frtypmode = models.CharField(max_length=1, blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'multipleconsigne_r_tbl'


class LraccounttransactionTTbl(models.Model):
    # lra_tran_id = models.AutoField(primary_key=True)
    lra_acc_id = models.IntegerField()
    lra_tran_no = models.CharField(max_length=25)
    lra_lr_no = models.CharField(max_length=18)
    lra_whm_code = models.CharField(max_length=4)
    lra_acc_code = models.CharField(max_length=5)
    lra_tr_date = models.DateTimeField()
    lra_gl_code = models.CharField(max_length=5)
    lra_vr_no = models.CharField(max_length=20)
    lra_tran_type = models.CharField(max_length=1)
    lra_cash = models.DecimalField(max_digits=18, decimal_places=2)
    lra_transfer = models.DecimalField(max_digits=18, decimal_places=2)
    lra_authorised = models.CharField(max_length=1)
    lra_makerid = models.CharField(max_length=10)
    lra_checkerid = models.CharField(max_length=10)
    lra_making_time = models.DateTimeField()
    lra_checking_time = models.DateTimeField()
    lra_cashier_id = models.CharField(max_length=10)
    lra_cashier_time = models.DateTimeField()
    lra_narration = models.CharField(max_length=200)
    lra_narration1 = models.CharField(max_length=200)

    # class Meta:
    #     managed = False
    #     db_table = 'lraccounttransaction_t_tbl'

# class Nextnumbercreator(models.Model):
#     # nnc_id = models.AutoField(primary_key=True)
#     nnc_desc = models.CharField(max_length=50, blank=True, null=True)
#     nnc_no = models.CharField(max_length=10, blank=True, null=True)
#     nnc_wrhcodepntr = models.IntegerField(blank=True, null=True)
#     nnc_code = models.CharField(max_length=10, blank=True, null=True)
#     nnc_slno = models.IntegerField(blank=True, null=True)
#     nnc_active = models.CharField(max_length=1, blank=True, null=True)
#     nnc_remarks = models.CharField(max_length=250, blank=True, null=True)
#     nnc_clntcode = models.IntegerField(blank=True, null=True)

#     # class Meta:
#     #     managed = False
#     #     db_table = 'nextnumbercreator'


# class Onetimecodemaster(models.Model):
#     # onetime_id = models.AutoField()
#     onetime_code = models.CharField(max_length=50, blank=True, null=True)
#     onetime_code_pntr = models.IntegerField(blank=True, null=True)
#     onetime_remarks = models.CharField(max_length=50, blank=True, null=True)

#     # class Meta:
#     #     managed = False
#     #     db_table = 'onetimecodemaster'


# class Onetimeconsignemaster(models.Model):
#     # onetime_id = models.AutoField(primary_key=True)
#     onetime_cnecode = models.IntegerField(blank=True, null=True)
#     ontime_name = models.CharField(max_length=150, blank=True, null=True)
#     onetime_address = models.TextField(blank=True, null=True)
#     onetime_city = models.CharField(max_length=150, blank=True, null=True)
#     onetime_lrno = models.CharField(max_length=150, blank=True, null=True)
#     onetime_tpno = models.CharField(max_length=150, blank=True, null=True)
#     onetime_whmpntr = models.IntegerField(blank=True, null=True)

#     # class Meta:
#     #     managed = False
#     #     db_table = 'onetimeconsignemaster'

class GenBranchdetailsPTbl(models.Model):
    genbr_code = models.CharField(max_length=4)
    genbr_name = models.CharField(max_length=50)
    genbr_address = models.CharField(max_length=50)
    genbr_phone1 = models.CharField(max_length=15)
    genbr_phone2 = models.CharField(max_length=15, blank=True, null=True)
    genbr_email = models.CharField(max_length=50, blank=True, null=True)
    genbr_acccode = models.CharField(max_length=18, blank=True, null=True)
    genbr_online = models.CharField(max_length=1, blank=True, null=True)
    genbr_onlinedate = models.DateTimeField(blank=True, null=True)
    genbr_dbname = models.CharField(max_length=50, blank=True, null=True)
    genbr_imagedbname = models.CharField(max_length=50, blank=True, null=True)
    genbr_logdbname = models.CharField(max_length=50, blank=True, null=True)
    genbr_servername = models.CharField(max_length=50, blank=True, null=True)
    gendistrict_name = models.CharField(max_length=50)
    genservice_area_code = models.CharField(max_length=50)
    gendistrict_code = models.CharField(max_length=50)
    genbr_dayendstatus = models.CharField(max_length=1)
    genbr_dayopenstatus = models.CharField(max_length=1)
    genbr_area = models.CharField(max_length=10)

    # class Meta:
    #     managed = False
    #     db_table = 'gen_branchdetails_p_tbl'


class GenTransnoPTbl(models.Model):
    trans_no = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'gen_transno_p_tbl'


class Genparameter(models.Model):
    # genpm_id = models.BigAutoField(primary_key=True)
    genpm_name = models.CharField(max_length=50, blank=True, null=True)
    genpm_value = models.CharField(max_length=2, blank=True, null=True)
    genpm_pntr = models.IntegerField(blank=True, null=True)
    genpm_slno = models.IntegerField(blank=True, null=True)
    genpm_active = models.CharField(max_length=1, blank=True, null=True)
    genpm_remarks = models.CharField(max_length=250, blank=True, null=True)
    genpm_makerid = models.IntegerField(blank=True, null=True)
    genpm_maketime = models.DateTimeField(blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'genparameter'


# class PickupcodePTbl(models.Model):
#     pkc_code = models.IntegerField()
#     pkc_type = models.IntegerField()
#     pkc_id = models.IntegerField()
#     pkc_description = models.CharField(max_length=75)
#     pkc_orderno = models.IntegerField()
#     pkc_parentid = models.IntegerField()
#     pkc_locked = models.CharField(max_length=1)

#     # class Meta:
#     #     managed = False
#     #     db_table = 'pickupcode_p_tbl'


# class PickuptypePTbl(models.Model):
#     pkt_code = models.IntegerField()
#     pkt_description = models.CharField(max_length=25)
#     pkt_parentid = models.IntegerField()
#     pkt_locked = models.CharField(max_length=1)

#     # class Meta:
#     #     managed = False
#     #     db_table = 'pickuptype_p_tbl'

# class StatuspTbl(models.Model):
#     # id = models.IntegerField()
#     text = models.CharField(max_length=10, blank=True, null=True)
#     value = models.CharField(max_length=2, blank=True, null=True)

#     # class Meta:
#     #     managed = False
#     #     db_table = 'statusp_tbl'