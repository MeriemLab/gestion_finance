from rest_framework import generics
from .models import Paiement
from .serializers import PaiementSerializer

class PaiementListCreate(generics.ListCreateAPIView):
    queryset = Paiement.objects.all()
    serializer_class = PaiementSerializer

class PaiementRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paiement.objects.all()
    serializer_class = PaiementSerializer
