from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Client
from .serializers import ClientSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework import status
from rest_framework import generics

class ClientListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ClientDetailView(RetrieveAPIView):
#     queryset = Client.objects.all()
#     serializer_class = ClientSerializer
#     lookup_field = 'pk' 

class ClientCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    

class ClientUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'pk'

class ClientDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'pk'

class VueListeClientsVIP(generics.ListAPIView):
    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.filter(est_vip=True)