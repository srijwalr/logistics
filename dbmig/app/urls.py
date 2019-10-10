from django.conf.urls import url
from . import views
# from app.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView


app_name = 'app'

urlpatterns = [
    # url(r'lr', views.lr, name='lr'),
    url(r'lorry-receipt/', views.LorryReceiptView.as_view(), name='lr'),
    url(r'validate', views.lr, name='validate'),
    url(r'podc', views.podc, name= 'podc'),
    url(r'signin',views.sign_in, name= 'sign_in'),
    url(r'register', views.register,name='register'),
    url(r'', views.dash,name='dash'),
    url(r'sign_out', views.sign_out,name='sign_out'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)