from django.db import models
from django.dispatch import receiver
from django.utils.timezone import now
from django.db.models.signals import pre_delete

# Create your models here.


# class Openingclosingbalance(models.Model):
#     # ocb_id = models.AutoField(primary_key=True)
#     ocb_date = models.DateField(blank=True, null=True)
#     ocb_opngbalnc = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
#     ocb_clsngbalnc = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
#     ocb_whmcode = models.IntegerField(blank=True, null=True)
#     ocb_opngdatetime = models.DateTimeField(blank=True, null=True)
#     ocb_opngusrid = models.IntegerField(blank=True, null=True)
#     ocb_clsngtime = models.DateTimeField(blank=True, null=True)
#     ocb_clsngusrid = models.IntegerField(blank=True, null=True)
#     ocb_status = models.CharField(max_length=1, blank=True, null=True)

#     # class Meta:
#     #     managed = False
#     #     db_table = 'openingclosingbalance'




class VoucherNumbersettings(models.Model):
    # vou_id = models.AutoField()
    vou_desc = models.CharField(max_length=50, blank=True, null=True)
    vou_no = models.CharField(max_length=10, blank=True, null=True)
    vou_wrhcodepntr = models.IntegerField(blank=True, null=True)
    vou_code = models.CharField(max_length=10, blank=True, null=True)
    vou_slno = models.IntegerField(blank=True, null=True)
    vou_active = models.CharField(max_length=1, blank=True, null=True)
    vou_remarks = models.CharField(max_length=250, blank=True, null=True)
    vou_clntcode = models.IntegerField(blank=True, null=True)
    vou_city = models.CharField(max_length=25, blank=True, null=True)
    
    def __str__(self):
        return str(self.vou_code)
    # class Meta:
    #     managed = False
    #     db_table = 'voucher_numbersettings'


class Accountstransactionlog(models.Model):
    # act_tranid = models.AutoField(primary_key=True)
    logact_tranno = models.CharField(max_length=50, blank=True, null=True)
    logact_reason = models.TextField(max_length=250)
    logact_userid = models.IntegerField(blank=True, null=True)
    logact_deltime = models.DateTimeField(blank=True, null=True )
    logact_lrno = models.TextField(blank=True, null=True)
    logact_whmcode = models.CharField(max_length = 10, blank=True, null=True)
    logact_acc_code = models.CharField(max_length=30, blank=True, null=True)
    logact_glcode = models.CharField(max_length=15, blank=True, null=True)
    logact_trandate = models.DateField(blank=True, null=True)
    logact_vrno = models.CharField(max_length = 20, blank=True, null=True)
    logact_trantype = models.CharField(max_length=1, blank=True, null=True)
    logact_month = models.CharField(max_length = 20, blank=True, null=True)
    logact_pay = models.TextField(blank=True, null=True)
    logact_cash_rcpt = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    logact_cash_pymnt = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    logact_transfer_rcpt = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    logact_transfer_pymnt = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    logact_narration = models.TextField(blank=True, null=True)
    logact_checkerid = models.IntegerField(blank=True, null=True)
    logact_makerid = models.IntegerField(blank=True, null=True)
    logact_makingtime = models.DateTimeField(blank=True, null=True)
    logact_checkingtime = models.DateTimeField(blank=True, null=True)


class Accountmaster(models.Model):

    acc_choices = (
        ('P', 'Payment'),
        ('R', 'Receipt'),
    )
    # acc_id = models.AutoField(primary_key=True)
    acc_name = models.CharField(max_length=200, blank=True, null=True)
    acc_shortname = models.CharField(max_length=10, blank=True, null=True)
    acc_category = models.CharField(choices = acc_choices, max_length=1, blank=True, null=True)
    acc_status = models.CharField(max_length=1, blank=True, null=True)
    acc_makerid = models.IntegerField(blank=True, null=True)
    acc_maketime = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.acc_name
    # class Meta:
    #     managed = False
    #     db_table = 'accountmaster'


class Accountswarehousemaster(models.Model):
    # accwm_id = models.AutoField(primary_key=True)
    accwm_desc = models.CharField(max_length=50, blank=True, null=True)
    accwm_name = models.CharField(max_length=150, blank=True, null=True)
    accwm_slno = models.IntegerField(blank=True, null=True)
    accwm_remarks = models.CharField(max_length=250, blank=True, null=True)
    accwm_active = models.CharField(max_length=2, blank=True, null=True)

    # class Meta:
    #     managed = False
    #     db_table = 'accountswarehousemaster'
    def __str__(self):
        return self.accwm_name
    

class Accountstransaction(models.Model):
    # act_tranid = models.AutoField(primary_key=True)

    Month_choices = (
            ('1', 'January'),
            ('2', 'February'),
            ('3', 'March'),
            ('4', 'April'),
            ('5', 'May'),                                                                                                                                    
            ('6', 'June'), 
            ('7', 'July'), 
            ('8', 'August'), 
            ('9', 'September'),
            ('10', 'October'),
            ('11', 'November'),
            ('12', 'December'),
        )
    act_tranno = models.CharField(max_length=50, blank=True, null=True)
    act_lrno = models.TextField(verbose_name = 'LR Number', blank=True, null=True)
    act_whmcode = models.ForeignKey(Accountswarehousemaster,blank=True, null=True, verbose_name = 'Warehouse',  on_delete = models.CASCADE)
    act_acc_code = models.ForeignKey(Accountmaster, verbose_name = 'Account Head',  on_delete = models.CASCADE)
    act_glcode = models.CharField(max_length=10, blank=True, null=True)
    act_trandate = models.DateField(blank=True, null=True)
    act_vrno = models.CharField(max_length = 20, blank=True, null=True, verbose_name = 'Voucher Number')
    act_trantype = models.CharField(max_length=1, blank=True, null=True)
    act_pay = models.CharField(max_length = 150, verbose_name = 'Pay To', blank=True, null=True)
    act_month = models.CharField(choices = Month_choices, max_length = 50, verbose_name = 'Expense For The Month')
    act_cash_rcpt = models.DecimalField(max_digits=18, default=0, decimal_places=2, verbose_name='Rupees', blank=True, null=True)
    act_cash_pymnt = models.DecimalField(max_digits=18, default=0, decimal_places=2, verbose_name = 'Rupees', blank=True, null=True)
    act_transfer_rcpt = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    act_transfer_pymnt = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    act_narration = models.TextField(verbose_name = 'Narration', blank=True, null=True)
    act_checkerid = models.IntegerField(blank=True, null=True)
    act_makerid = models.IntegerField(blank=True, null=True)
    act_makingtime = models.DateTimeField(blank=True, null=True, verbose_name='Voucher Date')
    act_checkingtime = models.DateTimeField(blank=True, null=True)
    act_balance = models.DecimalField(max_digits=18, decimal_places=2, default=0.00, verbose_name= 'Cash Balance')

    def save(self, *args, **kwargs):    
        # if not self.pk:  # object is being created, thus no primary key field yet
        self.act_balance -= self.act_cash_pymnt
        self.act_balance += self.act_cash_rcpt
        # self.act_vrno = '{}-{}'.format(self.foo_rel.foo_code, self.bar_code)
        super(Accountstransaction, self).save(*args, **kwargs)                                  

@receiver(pre_delete, sender=Accountstransaction)
def _pre_delete_receiver(sender, instance, **kwargs):
    # instance = Lrtransation.objects.get(id = 'id')
    # kwargs = model_to_dict(instance, exclude=['id','lrtran_driverdtls'])

    new_instance = Accountstransactionlog()

    new_instance.logact_tranno = instance.act_tranno
    new_instance.logact_lrno = instance.act_lrno
    new_instance.logact_whmcode = str(instance.act_whmcode)
    new_instance.logact_acc_code = instance.act_acc_code
    new_instance.logact_glcode = instance.act_glcode
    new_instance.logact_trandate = instance.act_trandate
    new_instance.logact_vrno = str(instance.act_vrno)
    new_instance.logact_trantype = instance.act_trantype
    new_instance.logact_month = instance.act_month
    new_instance.logact_pay = instance.act_pay
    new_instance.logact_cash_rcpt = instance.act_cash_rcpt
    new_instance.logact_cash_pymnt = instance.act_cash_pymnt
    new_instance.logact_transfer_rcpt = instance.act_transfer_rcpt
    new_instance.logact_transfer_pymnt = instance.act_transfer_pymnt
    new_instance.logact_narration = instance.act_narration
    new_instance.logact_checkerid = instance.act_checkerid
    new_instance.logact_makerid = instance.act_makerid
    new_instance.logact_makingtime = instance.act_makingtime
    new_instance.logact_checkingtime = instance.act_checkingtime

    new_instance.save()

