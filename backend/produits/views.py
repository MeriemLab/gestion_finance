from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated
from .models import Produit
from .serializers import ProduitSerializer
from rest_framework.generics import CreateAPIView
from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
class ProduitListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer


class ProduitCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProduitSerializer
class ProduitDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer
    
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)