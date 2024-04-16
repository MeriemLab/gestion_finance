from .models import Factureservice
from .serializers import  FactureserviceSerializer
from rest_framework.generics import ListAPIView,  CreateAPIView, UpdateAPIView 

class  FactureserviceListView(ListAPIView):
    queryset = Factureservice.objects.all()
    serializer_class = FactureserviceSerializer

class FactureserviceCreateView(CreateAPIView):
    queryset = Factureservice.objects.all()
    serializer_class = FactureserviceSerializer

class FactureserviceUpdateView(UpdateAPIView):
    queryset = Factureservice.objects.all()
    serializer_class = FactureserviceSerializer
