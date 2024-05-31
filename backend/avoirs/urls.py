from django.urls import path
from .views import AvoirDetailAndCreateAPIView, AvoirListAPIView, AvoirVenteListAPIView, AvoirServiceListAPIView

urlpatterns = [
    path('facturesvente/<int:pk>/avoirs/', AvoirDetailAndCreateAPIView.as_view(), {'type_facture': 'Vente'}, name='avoirs-vente-facture-detail'),
    path('facturesservice/<int:pk>/avoirs/', AvoirDetailAndCreateAPIView.as_view(), {'type_facture': 'Service'}, name='avoirs-service-facture-detail'),
    path('avoirs/', AvoirListAPIView.as_view(), name='avoirs-list'),
    path('avoirs/vente/', AvoirVenteListAPIView.as_view(), name='avoirs-vente-list'),
    path('avoirs/service/', AvoirServiceListAPIView.as_view(), name='avoirs-service-list'),
]
