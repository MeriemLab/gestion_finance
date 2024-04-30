from django.urls import path
from .views import FactureServiceListView , FactureServiceCreateView , FactureServiceUpdateView , PDFFactureView,VueListeNonpayée
from .views import FactureVenteListView,  FactureVenteCreateView, FactureVenteUpdateView , PDFFactureView,VueListeNonpayée


urlpatterns = [
    path('factures_service/', FactureServiceListView.as_view(), name='facture-list'),
    
    path('factures_service/create/', FactureServiceCreateView.as_view(), name='facture-create'),  
    path('factures_service/<int:pk>/update/', FactureServiceUpdateView.as_view(), name='facture-update'),
    path('factures_service/<int:id>/pdf/', PDFFactureView.as_view(), name='facture-pdf'),
    path('factures_vente/', FactureVenteListView.as_view(), name='facture-list'),
    path('factures_vente/create/', FactureVenteCreateView.as_view(), name='facture-create'),
    path('factures_vente/<int:pk>/update/', FactureVenteUpdateView.as_view(), name='facture-update'),
    path('factures_vente/<int:id>/pdf/', PDFFactureView.as_view(), name='facture-pdf'),
    path('Non-payées/', VueListeNonpayée.as_view(), name='liste_factures_nonpayée'),

]



