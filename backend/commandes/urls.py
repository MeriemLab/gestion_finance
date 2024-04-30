
# ]
from django.urls import path
from .views import (
    commandesListView, commandesDetailView, commandesCreateView,
    # commandesUpdateView, commandesDeleteView,
    commandes_ligneListView, commandes_ligneDetailView, commandes_ligneCreateView,
    #commandes_ligneUpdateView, commandes_ligneDeleteView

)

urlpatterns = [
    path('commandess/', commandesListView.as_view(), name='commandes-list'),
    path('commandess/<int:pk>/', commandesDetailView.as_view(), name='commandes-detail'),
    path('commandess/create/', commandesCreateView.as_view(), name='commandes-create'),
    #path('commandess/<int:pk>/update/', commandesUpdateView.as_view(), name='commandes-update'),
    #path('commandess/<int:pk>/delete/', commandesDeleteView.as_view(), name='commandes-delete'),
    
    

    path('commandes_lignes/', commandes_ligneListView.as_view(), name='commandes_ligne-list'),
    path('commandes_lignes/<int:pk>/', commandes_ligneDetailView.as_view(), name='commandes_ligne-detail'),
    path('commandes_lignes/create/', commandes_ligneCreateView.as_view(), name='commandes_ligne-create'),
    #path('commandes_lignes/<int:pk>/update/', commandes_ligneUpdateView.as_view(), name='commandes_ligne-update'),
    #path('commandes_lignes/<int:pk>/delete/', commandes_ligneDeleteView.as_view(), name='commandes_ligne-delete'),
    
]
