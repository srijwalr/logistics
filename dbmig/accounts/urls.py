from django.conf.urls import url
from accounts import views
from accounts.views import TransactionView, ReceiptView, AccountsCreate
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

app_name = 'accounts'

urlpatterns = [
    # url(r'vduplicate',views.copy,name='copy'),
    url(r'voucher',views.TransactionView.as_view(), name='voucher'),
    url(r'receipt',views.ReceiptView.as_view(), name='receipt'),
    url(r'acchead',views.AccountsCreate.as_view(), name='acchead'),   
    url(r'dlt',views.vrdelete, name='delete'), 
    url(r'dplct',views.vrdata,name='dplct'),
    # url(r'^(?P<accountstransaction_id>[0-9]+)/delete_voucher/$', views.vrdelete, name='vchrdlt'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)