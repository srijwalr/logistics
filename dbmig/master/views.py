from django.shortcuts import render
from master.forms import CosingneemasterForm , ProductmasterForm
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy


class ConsigneeView(FormView):
    import pdb; pdb.set_trace()
    template_name = 'consignee.html'
    form_class = CosingneemasterForm
    success_url = reverse_lazy('master:consignee')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["vehicle_types"] =  
        # import pdb;pdb.set_trace()
        return context



def productcategory(request):
    form = ProductmasterForm()
    return render(request, 'productcategory.html', {'form': form})


def productsubcategory(request):
    form = ProductmasterForm()
    return render(request, 'productsubcategory.html', {'form': form})


class ProductView(TemplateView):
    template_name = 'product.html'

