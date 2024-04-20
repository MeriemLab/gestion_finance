from rest_framework import generics
from .models import FactureVente, FactureService, Paiement
from .serializers import FactureVenteSerializer, FactureServiceSerializer, PaiementSerializer

class FactureVenteListCreate(generics.ListCreateAPIView):
    queryset = FactureVente.objects.all()
    serializer_class = FactureVenteSerializer

class FactureServiceListCreate(generics.ListCreateAPIView):
    queryset = FactureService.objects.all()
    serializer_class = FactureServiceSerializer

class PaiementListCreate(generics.ListCreateAPIView):
    queryset = Paiement.objects.all()
    serializer_class = PaiementSerializer

class PaiementRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paiement.objects.all()
    serializer_class = PaiementSerializer
