from django.urls import path
from .views import (
 PaiementListCreate, PaiementRetrieveUpdateDestroy
)

urlpatterns = [
  
    path('paiements/', PaiementListCreate.as_view(), name='paiement-list-create'),
    path('paiements/<int:pk>/', PaiementRetrieveUpdateDestroy.as_view(), name='paiement-detail'),
]
