from django.urls import path
from .views import (
    FactureVenteListCreate, FactureServiceListCreate, PaiementListCreate, PaiementRetrieveUpdateDestroy
)

urlpatterns = [
    path('factures_ventee/', FactureVenteListCreate.as_view(), name='facture-vente-list-create'),
    path('factures_servicee/', FactureServiceListCreate.as_view(), name='facture-service-list-create'),
    path('paiements/', PaiementListCreate.as_view(), name='paiement-list-create'),
    path('paiements/<int:pk>/', PaiementRetrieveUpdateDestroy.as_view(), name='paiement-detail'),
]
