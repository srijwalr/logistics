from django.conf.urls import url
from . import views
# from app.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


app_name = 'app'

urlpatterns = [
    url(r'lorry-receipt/', views.LorryReceiptView.as_view(), name='lr'),
    url(r'validate', views.validate, name='validate'),
    url(r'print/$', views.MyModelPrintView.as_view(), name='print'),
    url(r'podc', views.LrdocumentCreate.as_view(), name= 'podc'),
    url(r'pod', views.pod, name= 'pod'),
    url(r'signin', views.sign_in,name='signin'),
    url(r'whm', views.WhmCreate.as_view(),name='whm'),
    url(r'^$',views.dash, name= 'dash'),
    url(r'register', views.register,name='register'),
    url(r'signout', views.LogoutView.as_view(),name='signout'),
    url(r'delete', views.deletelr,name='deletelr'),
    url(r'change', views.change,name='change'),
    url(r'duplicate', views.duplicate,name='duplicate'),
    url(r'editvno', views.editvno,name='editvno'),
    # url(r'delete_lr/$', views.delete_,name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)