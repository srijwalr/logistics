from django.db import models

# Create your models here.
class Cosingneemaster(models.Model):
    # consgnemid = models.IntegerField( blank=True, null=True)
    consgnem_code = models.CharField(max_length=50, blank=True, null=True)
    consgnem_name = models.CharField(max_length=100, blank=True, null=True)
    consgnem_branch = models.CharField(max_length=50, blank=True, null=True)
    consgnem_address = models.CharField(max_length=500, blank=True, null=True)
    consgnem_city = models.CharField(max_length=50, blank=True, null=True)
    consgnem_district = models.CharField(max_length=50, blank=True, null=True)
    consgnem_pincode = models.IntegerField(blank=True, null=True)
    consgnem_routtyp = models.CharField(max_length=20, blank=True, null=True)
    consgnem_gsttin = models.CharField(max_length=25, blank=True, null=True)
    consgnem_pan = models.CharField(max_length=25, blank=True, null=True)
    consgnem_distance = models.FloatField(blank=True, null=True)
    cosngnrm_slno = models.IntegerField(blank=True, null=True)
    consgnem_remarks = models.CharField(max_length=250, blank=True, null=True)
    consgnem_active = models.CharField(max_length=1, blank=True, null=True)
    consgnem_makerid = models.IntegerField(blank=True, null=True)
    consgnem_maketime = models.DateTimeField(blank=True, null=True)
    consgnem_routepntr = models.IntegerField(blank=True, null=True)
    consgnem_clntpntr = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     db_table = 'cosingneemaster'

class Productcategory(models.Model):
    # procat_id = models.IntegerField( blank=True, null=True)
    procat_code = models.CharField(max_length=25, blank=True, null=True)
    procat_desc = models.CharField(max_length=100, blank=True, null=True)
    procat_slno = models.IntegerField(blank=True, null=True)
    procat_active = models.CharField(max_length=1, blank=True, null=True)
    procat_remarks = models.CharField(max_length=250, blank=True, null=True)
    procat_makerid = models.IntegerField(blank=True, null=True)
    procat_maketime = models.DateTimeField(blank=True, null=True)
    procat_clntpntr = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     db_table = 'productcategory'


class Productsubcategory(models.Model):
    # proscat_id = models.IntegerField(blank=True, null=True )
    proscat_procatpntr = models.ForeignKey(Productcategory,  on_delete = models.CASCADE)
    proscat_code = models.CharField(max_length=50, blank=True, null=True)
    proscat_desc = models.CharField(max_length=100, blank=True, null=True)
    proscat_volume = models.FloatField(blank=True, null=True)
    proscat_weight = models.FloatField(blank=True, null=True)
    proscat_width = models.FloatField(blank=True, null=True)
    proscat_length = models.FloatField(blank=True, null=True)
    proscat_slno = models.IntegerField(blank=True, null=True)
    proscat_active = models.CharField(max_length=1, blank=True, null=True)
    proscat_remarks = models.CharField(max_length=250, blank=True, null=True)
    proscat_makerid = models.IntegerField(blank=True, null=True)
    proscat_maketime = models.DateTimeField(blank=True, null=True)
    proscat_clntcode = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     db_table = 'productsubcategory'


class Productgroup(models.Model):
    # prog_id = models.AutoField(primary_key=True)
    prog_code = models.CharField(max_length=50, blank=True, null=True)
    prog_desc = models.CharField(max_length=150, blank=True, null=True)
    prog_slno = models.IntegerField(blank=True, null=True)
    prog_rmrks = models.TextField(blank=True, null=True)
    prog_status = models.CharField(max_length=1, blank=True, null=True)
    prog_clntpntr = models.IntegerField(blank=True, null=True)
    
    # class Meta:
    #     db_table = 'productgroup'

class Productmaster(models.Model):
    # promas_id = models.IntegerField( blank=True, null=True)
    promas_code = models.CharField(max_length=50, blank=True, null=True)
    promas_desc = models.CharField(max_length=100, blank=True, null=True)
    promas_quantity = models.IntegerField(blank=True, null=True)
    promas_procat_pntr = models.ForeignKey(Productcategory,  on_delete = models.CASCADE)
    promas_proscat_pntr = models.ForeignKey(Productsubcategory,  on_delete = models.CASCADE)
    promas_group_pntr = models.ForeignKey(Productgroup, on_delete = models.CASCADE)
    promas_slno = models.IntegerField(blank=True, null=True)
    promas_active = models.CharField(max_length=1, blank=True, null=True)
    promas_remarks = models.CharField(max_length=250, blank=True, null=True)
    promas_makerid = models.IntegerField(blank=True, null=True)
    promas_maketime = models.DateTimeField(blank=True, null=True)
    promas_clntcode = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     db_table = 'productmaster'        

class Vehiclecategory(models.Model):
    # vehcat_id = models.IntegerField( blank=True, null=True)
    vehcat_code = models.CharField(max_length=50, blank=True, null=True)
    vehcat_desc = models.CharField(max_length=100, blank=True, null=True)
    vehcat_wtcapacity = models.FloatField(blank=True, null=True)
    vehcat_length = models.FloatField(blank=True, null=True)
    vehcat_width = models.FloatField(blank=True, null=True)
    vehcat_ft = models.CharField(max_length=50, blank=True, null=True)
    vehcat_kmrate = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    vehcat_slno = models.IntegerField(blank=True, null=True)
    vehcat_active = models.CharField(max_length=1, blank=True, null=True)
    vehcat_remarks = models.CharField(max_length=250, blank=True, null=True)
    vehcat_makerid = models.IntegerField(blank=True, null=True)
    vehcat_maketime = models.DateTimeField(blank=True, null=True)

    # class Meta:
    #     db_table = 'vehiclecategory'

class Vehiclemaster(models.Model):
    # vehmas_id = models.IntegerField( blank=True, null=True)
    vehmas_code = models.CharField(max_length=50, blank=True, null=True)
    vehmas_desc = models.CharField(max_length=100, blank=True, null=True)
    vehmas_catpntr = models.ForeignKey(Vehiclecategory,  on_delete = models.CASCADE)
    vehmas_frtyppntr = models.IntegerField(blank=True, null=True)
    vehmas_modepntr = models.IntegerField(blank=True, null=True)
    vehmas_slno = models.IntegerField(blank=True, null=True)
    vehmas_active = models.CharField(max_length=1, blank=True, null=True)
    vehmas_remarks = models.CharField(max_length=250, blank=True, null=True)
    vehmas_makerid = models.IntegerField(blank=True, null=True)
    vehmas_maketime = models.DateTimeField(blank=True, null=True)
    vehmas_clntpntr = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     db_table = 'vehiclemaster'


class Freighttypes(models.Model):
    # fretype_id = models.IntegerField( blank=True, null=True)
    fretype_code = models.CharField(max_length=50, blank=True, null=True)
    fretype_desc = models.CharField(max_length=100, blank=True, null=True)
    fretype_slno = models.IntegerField(blank=True, null=True)
    fretype_remarks = models.CharField(max_length=250, blank=True, null=True)
    fretype_active = models.CharField(max_length=1, blank=True, null=True)
    fretype_nnc_code = models.CharField(max_length=10, blank=True, null=True)
    fretype_whmcode = models.IntegerField(blank=True, null=True)

    # class Meta:
    #     db_table = 'freighttypes'

class Routemaster(models.Model):
    # rtm_id = models.IntegerField( blank=True, null=True)
    rtm_code = models.CharField(max_length=50, blank=True, null=True)
    rtm_desc = models.CharField(max_length=100)
    rtm_dist = models.CharField(max_length=50)
    rtm_slno = models.IntegerField(blank=True, null=True)
    rtm_remarks = models.CharField(max_length=250, blank=True, null=True)
    rtm_active = models.CharField(max_length=1, blank=True, null=True)
    rtm_details = models.CharField(max_length=250, blank=True, null=True)

    # class Meta:
    #     db_table = 'routemaster'


class Freightforroute(models.Model):
    # fght_id = models.BigIntegerField( blank=True, null=True)
    fght_fretypeptr = models.IntegerField(blank=True, null=True)
    fght_routeptr = models.IntegerField(blank=True, null=True)
    fght_basefreight = models.IntegerField(blank=True, null=True)
    fght_kmrate = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    fght_vehcatptr = models.IntegerField(blank=True, null=True)
    fght_slno = models.IntegerField(blank=True, null=True)
    fght_remarks = models.CharField(max_length=250, blank=True, null=True)
    fght_active = models.CharField(max_length=1, blank=True, null=True)

    # class Meta:
    #     db_table = 'freightforroute'