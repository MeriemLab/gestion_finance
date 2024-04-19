from django.urls import path
from .views import FactureListCreate, PaiementListCreate, PaiementRetrieveUpdateDestroy

urlpatterns = [
    path('factures/', FactureListCreate.as_view(), name='facture-list-create'),
    path('paiements/', PaiementListCreate.as_view(), name='paiement-list-create'),
    path('paiements/<int:pk>/', PaiementRetrieveUpdateDestroy.as_view(), name='paiement-detail'),
]