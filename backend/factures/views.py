from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView,  CreateAPIView, UpdateAPIView 
from rest_framework import generics
from .models import Facture
from .serializers import FactureSerializer

class FactureListView(ListAPIView):
    
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer

class FactureListCreate(CreateAPIView):
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer

# class FactureDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Facture.objects.all()
#     serializer_class = FactureSerializer

class FactureVenteList(generics.ListAPIView):
    queryset = Facture.objects.filter(type_facture='Vente')
    serializer_class = FactureSerializer

class FactureServiceList(generics.ListAPIView):
    queryset = Facture.objects.filter(type_facture='Service')
    serializer_class = FactureSerializer

class FactureNonPayeeList(generics.ListAPIView):
    serializer_class = FactureSerializer

    def get_queryset(self):
        return Facture.objects.filter(non_payee=True)