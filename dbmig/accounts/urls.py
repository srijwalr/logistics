from django.conf.urls import url
from . import views
from accounts.views import *
from accounts.views import TransactionView, ReceiptView, AccountsCreate
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

app_name = 'accounts'

urlpatterns = [
    url(r'voucher',views.TransactionView.as_view(), name='voucher'),
    url(r'receipt',views.ReceiptView.as_view(), name='receipt'),
    url(r'duplicate',views.duplicate,name='duplicate'),
    url(r'delete',views.vrdata, name='delete'),
    url(r'acchead',views.AccountsCreate.as_view(), name='acchead'),    
    url(r'^(?P<accountstransaction_id>[0-9]+)/delete_voucher/$', views.vrdelete, name='vchrdlt'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)