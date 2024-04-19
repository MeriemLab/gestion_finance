from rest_framework import generics
from .models import Facture, Paiement
from .serializers import FactureSerializer, PaiementSerializer

class FactureListCreate(generics.ListCreateAPIView):
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer

class PaiementListCreate(generics.ListCreateAPIView):
    queryset = Paiement.objects.all()
    serializer_class = PaiementSerializer

class PaiementRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paiement.objects.all()
    serializer_class = PaiementSerializer