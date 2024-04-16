from django.urls import path
from .views import FactureserviceListView,FactureserviceCreateView,FactureserviceUpdateView


urlpatterns = [
    path('factures_service/', FactureserviceListView.as_view(), name='facture-list'),
    
    path('factures_service/create/', FactureserviceCreateView.as_view(), name='facture-create'),  
    path('factures_service/<int:pk>/update/', FactureserviceUpdateView.as_view(), name='facture-update'),  ]
