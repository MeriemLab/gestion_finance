from django.urls import path
from .views import (
    ClientListView, ClientDetailView, ClientCreateView,
    ClientUpdateView, ClientDeleteView, VueListeClientsVIP
)

urlpatterns = [
    path('clients/', ClientListView.as_view(), name='client-list'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    path('clients/create/', ClientCreateView.as_view(), name='client-create'),
    path('clients/<int:pk>/update/', ClientUpdateView.as_view(), name='client-update'),
    path('clients/<int:pk>/delete/', ClientDeleteView.as_view(), name='client-delete'),
    path('clients-vip/', VueListeClientsVIP.as_view(), name='liste_clients_vip'),
]