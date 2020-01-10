from django import forms
from accounts.models import Accountstransaction

class AccountTransactionForm(forms.ModelForm):
    act_balance = forms.CharField(widget = forms.TextInput(attrs={'readonly':'readonly'}))

    class Meta:
        model = Accountstransaction
        fields = ('act_whmcode', 'act_vrno','act_pay','act_month','act_acc_code','act_lrno','act_narration','act_cash_rcpt','act_balance')

        def __init__(self, *args, **kwargs):
            super(AccountTransactionForm, self).__init__(*args, **kwargs)
            instance = getattr(self, 'instance', None)
            if instance and instance.pk:
                self.fields['act_balance'].widget.attrs['readonly'] = True
                self.fields['act_balance'].queryset = Accountstransaction.objects.none()       


        def clean_act_balance(self):
            instance = getattr(self, 'instance', None)
            if instance and instance.pk:
                return instance.act_balance
            else:
                return self.cleaned_data['act_balance']  


        # def clean_act_balance(self):
        #     instance = getattr(self, 'instance', None)
        #     if instance and instance.pk:
        #         return instance.act_balance
        #     else:
        #         return self.cleaned_data['act_balance'] 
                