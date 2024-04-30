
from rest_framework.generics import ListAPIView
from .models import Commande
from .serializers import CommandeSerializer
from .serializers import Commande_ligneSerializer
from .models import Commande_ligne
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response

class commandesListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer
class commandesCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CommandeSerializer
class commandesDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Commande.objects.all()
    serializer_class = CommandeSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class commandes_ligneListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset =Commande_ligne.objects.all()
    serializer_class = Commande_ligneSerializer
class commandes_ligneCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = Commande_ligneSerializer
class commandes_ligneDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Commande_ligne.objects.all()
    serializer_class = Commande_ligneSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)