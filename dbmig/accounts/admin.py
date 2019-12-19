from django.contrib import admin
from accounts.models import Accountmaster, Accountstransaction, Accountswarehousemaster, Accountstransactionlog, VoucherNumbersettings
# Register your models here.
admin.site.register(Accountmaster)
admin.site.register(Accountstransaction)
admin.site.register(Accountswarehousemaster)
admin.site.register(Accountstransactionlog)
admin.site.register(VoucherNumbersettings)


