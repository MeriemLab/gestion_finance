from django.urls import path
from .views import FactureVenteListView,  FactureVenteCreateView, FactureVenteUpdateView

urlpatterns = [
    path('factures_vente/', FactureVenteListView.as_view(), name='facture-list'),
  
    path('factures_vente/create/', FactureVenteCreateView.as_view(), name='facture-create'),
    path('factures_vente/<int:pk>/update/', FactureVenteUpdateView.as_view(), name='facture-update'),
]
