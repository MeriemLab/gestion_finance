from django.contrib import admin
from django.urls import path, include
#from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('clients.urls')),
    
    path('api-auth/',include('rest_framework.urls')),
    #path('api/', include('factures_vente.urls')),
    #path('api/', include('factures_service.urls')),
    path('api/', include('devises.urls')),
    #path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
   # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('paiements.urls')),
    path('api/', include('authentification.urls')),
     path('api/', include('commandes.urls')),
    path('api/', include('paiements.urls')),
    path('api/', include('produits.urls')),
    #path('api/', include('commande_ligne.urls')),
    #path('api/', include('statistiques.urls')),
    path('api/', include('factures.urls')),
]