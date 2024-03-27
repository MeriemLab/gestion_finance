from django.urls import path
from .views import (
    factureListView,  # Utiliser le nom correctement importé
    factureDetailView,
    factureCreateView,
    factureUpdateView,
    factureDeleteView
)

urlpatterns = [
    path('facture/', factureListView.as_view(), name='facture-list'),
    path('facture/<int:pk>/', factureDetailView.as_view(), name='facture-detail'),
    path('facture/create/', factureCreateView.as_view(), name='facture-create'),
    path('facture/<int:pk>/update/', factureUpdateView.as_view(), name='facture-update'),
    path('facture/<int:pk>/delete/', factureDeleteView.as_view(), name='facture-delete'),
]