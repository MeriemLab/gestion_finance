from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Client
from .serializers import ClientSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response




class ClientListView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetailView(RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'pk'  # Champ utilisÃ© pour la recherche par ID

class ClientCreateView(CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientUpdateView(UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'pk'

class ClientDeleteView(DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'pk'

class VueListeClientsVIP(generics.ListAPIView):
    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.filter(est_vip=True)