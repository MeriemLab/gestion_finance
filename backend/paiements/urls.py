from django.urls import path
from .views import  ListePaiements ,PaiementCreateView

urlpatterns = [
    path('paiements/', ListePaiements.as_view(), name='liste-paiements'),
    path('factures/<int:pk>/paiements/', PaiementCreateView.as_view(), name='paiement-create'),
 
  
]