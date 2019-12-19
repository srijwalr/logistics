from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()
urlpatterns = [
    path('admin/', admin.site.urls),
    url('', include('app.urls')),
    url('accounts/', include('accounts.urls')),
    url('master/', include('master.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    