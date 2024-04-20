from django.urls import path
from .views import FactureServiceListView,FactureServiceCreateView,FactureServiceUpdateView


urlpatterns = [
    path('factures_service/', FactureServiceListView.as_view(), name='facture-list'),
    
    path('factures_service/create/', FactureServiceCreateView.as_view(), name='facture-create'),  
    path('factures_service/<int:pk>/update/', FactureServiceUpdateView.as_view(), name='facture-update'),  ]
