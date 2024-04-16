from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from clients import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('clients.urls')),  # Inclure les URLs de l'application clients
    path('api/', include('factures_vente.urls')),
   path('api/', include('factures_service.urls')),
]