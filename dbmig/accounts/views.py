from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView, CreateView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from accounts.models import Accountstransaction, Accountmaster
from accounts.forms import AccountTransactionForm
from django.db.models import Sum
import datetime
from django.db.models import Q


# Create your views here.
# class TransactionView(TemplateView):
    # import pdb; pdb.set_trace()
    # template_name = 'transaction.html'
    # form_class = CosingneemasterForm
    # success_url = reverse_lazy('app:dash')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # context["vehicle_types"] =  
    #     # import pdb;pdb.set_trace()
    #     return context

class TransactionView(CreateView):
    # import pdb; pdb.set_trace()
    model  = Accountstransaction
    template_name = 'transaction.html'  
    success_url = reverse_lazy('app:dash')
    fields = ('act_whmcode','act_vrno','act_pay','act_month','act_acc_code','act_lrno','act_narration','act_cash_pymnt','act_balance') 


class ReceiptView(CreateView):
    # model  = Accountstransaction
    template_name = 'receipt.html'
    form_class = AccountTransactionForm
    success_url = reverse_lazy('app:dash')
    # fields = ('act_whmcode', 'act_vrno','act_pay','act_month','act_acc_code','act_narration','act_cash_pymnt',) 


    def get_context_data(self, **kwargs):
        context = super(ReceiptView, self).get_context_data(**kwargs)
        context['form1'] = AccountTransactionForm
        return context

def copy(request):
    vouchers = Accountstransaction.objects.none()
    query = request.GET.get("q")
    print(query)
    if query:
        vouchers = Accountstransaction.objects.all()
        vouchers = vouchers.filter(
            Q(act_vrno__icontains=query)
        ).distinct()
        return render(request, 'vrdp.html', {
            'vouchers': vouchers,
        })
    else:
        return render(request, 'vchrdplct.html', {'vouchers': vouchers})

 

def vrdata(request):
    vouchers = Accountstransaction.objects.none()
    query = request.GET.get("q")
    print(query)
    if query:
        vouchers = Accountstransaction.objects.all()
        vouchers = vouchers.filter(
            Q(act_vrno__icontains=query)
        ).distinct()
        return render(request, 'vrdp.html', {
            'vouchers': vouchers,
        })
    else:
        return render(request, 'vchrdplct.html', {'vouchers': vouchers})  
     


def vrdelete(request):
    results = Accountstransaction.objects.none()
    query = request.GET.get("q")
    print(query)
    if query:
        results = Accountstransaction.objects.all()
        results = results.filter(
            Q(act_vrno__icontains=query)
        ).distinct()
        return render(request, 'vrdelete.html', {
            'lrdtls': results,
        })
    else:
        return render(request, 'vrdelete.html', {'lrdtls': results})


class AccountsCreate(CreateView):
    model = Accountmaster
    template_name = 'acchead.html'
    success_url = reverse_lazy('app:dash')
    fields = ('acc_name','acc_category')

