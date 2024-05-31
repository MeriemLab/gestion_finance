from django.urls import path
from .views import (
    ClientListView, ClientDetailView, 
    ClientCreateView,ClientDeleteView, 
    VueListeClientsVIP ,FacturesClientAPIView ,
    PaiementHistoryView , HistouriqueView
)

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('clients/create/', ClientCreateView.as_view(), name='client-create'),
    
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client-delete'),
    path('clients-vip/', VueListeClientsVIP.as_view(), name='liste_clients_vip'),
    path('clients/<int:client_id>/factures/', FacturesClientAPIView.as_view(), name='factures_client_api'),
    path('clients/<int:client_id>/paiements/', PaiementHistoryView.as_view(), name='client_paiement_history'),
    path('clients/<int:client_id>/historique/', HistouriqueView.as_view(), name='client_history'),
]