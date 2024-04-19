from django.urls import path
from .views import (
    DeviseListView, DeviseDetailView, DeviseCreateView,
    DeviseUpdateView, DeviseDeleteView
)

urlpatterns = [
    path('devises/', DeviseListView.as_view(), name='Devise-list'),
    path('devises/<int:pk>/', DeviseDetailView.as_view(), name='Devise-detail'),
    path('devises/create/', DeviseCreateView.as_view(), name='Devise-create'),
    path('devises/<int:pk>/update/', DeviseUpdateView.as_view(), name='Devise-update'),
    path('devises/<int:pk>/delete/', DeviseDeleteView.as_view(), name='Devise-delete'),
    
]