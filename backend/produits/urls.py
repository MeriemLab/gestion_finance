from django.urls import path
from .views import ProduitListView,ProduitCreateView,ProduitDetailView

urlpatterns = [
    path('produits/', ProduitListView.as_view(), name='produit-list'),
    path('produits/ajouter/', ProduitCreateView.as_view(), name='produit-create'),
    path('produits/<int:pk>/', ProduitDetailView.as_view(), name='produits-detail'),
]
