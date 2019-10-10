from django.conf.urls import url
from . import views
from master.views import ConsigneeView
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

app_name = 'master'

urlpatterns = [

    url(r'product', TemplateView.as_view(template_name='master/product.html')),
    # url(r'dashboard', views.dash, name= 'dash'),
    # url(r'userregister', views.register, name= 'reg'),
    url(r'^$', views.ConsigneeView.as_view(), name= 'consignee'),
    # url(r'product', views.product, name= 'product'),
    # url(r'productcat', views.productcat, name= 'productcat'),
    # url(r'psubcat', views.psubcat, name= 'psubcat'),
    # url(r'vehicle', views.vehicle, name= 'vehicle'),
    # url(r'vehicletype', views.vehicletype, name= 'vtype'),
    # url(r'freighttype', views.freighttype, name= 'ftype'),
    # url(r'route', views.route, name= 'route'),
    # url(r'froute', views.froute, name= 'froute'),
    # url(r'', views.login, name= 'login'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)