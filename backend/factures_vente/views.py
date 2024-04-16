from .models import FactureVente
from .serializers import FactureVenteSerializer
from rest_framework.generics import ListAPIView,  CreateAPIView, UpdateAPIView 

class FactureVenteListView(ListAPIView):
    queryset = FactureVente.objects.all()
    serializer_class = FactureVenteSerializer

class FactureVenteCreateView(CreateAPIView):
    queryset = FactureVente.objects.all()
    serializer_class = FactureVenteSerializer

class FactureVenteUpdateView(UpdateAPIView):
    queryset = FactureVente.objects.all()
    serializer_class = FactureVenteSerializer
