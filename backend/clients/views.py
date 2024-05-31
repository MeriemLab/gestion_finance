from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView,  DestroyAPIView
from .models import Client
from .serializers import ClientSerializer , ClientAjoutSerializer

from rest_framework.permissions import AllowAny,IsAuthenticated ,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import permissions

from rest_framework import status
from rest_framework import generics 

from factures.models import Facture
from factures.serializers import FactureSerializer

from paiements.models import Paiement
from paiements.serializers import PaiementSerializer
from rest_framework.views import APIView




class HistouriqueView(APIView):
    def get(self, request, client_id):
        # Récupère toutes les factures du client
        factures = Facture.objects.filter(client_id=client_id)
        factures_serializer = FactureSerializer(factures, many=True)

        # Récupère tous les paiements du client
        paiements = Paiement.objects.filter(facture__client_id=client_id)
        paiements_serializer = PaiementSerializer(paiements, many=True)

        # Crée une réponse JSON contenant les factures et les paiements
        data = {
            'factures': factures_serializer.data,
            'paiements': paiements_serializer.data,
        }
        return Response(data)

class PaiementHistoryView(APIView):
    def get(self, request, client_id):
        # Récupère toutes les factures du client
        factures = Facture.objects.filter(client_id=client_id)

        # Initialise une liste vide pour stocker les paiements
        paiements = []

        # Pour chaque facture du client, récupère tous les paiements associés
        for facture in factures:
            paiements_facture = Paiement.objects.filter(facture=facture)
            paiements.extend(paiements_facture)

        # Serialize les paiements récupérés
        serializer = PaiementSerializer(paiements, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PaiementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ClientListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
   

class ClientDetailView(generics.RetrieveUpdateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 

class ClientCreateView(CreateAPIView):
    # permission_classes = (AllowAny,)
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientAjoutSerializer
 

class ClientDeleteView(DestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'pk'

class VueListeClientsVIP(generics.ListAPIView):
    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.filter(est_vip=True)
    
class FacturesClientAPIView(ListAPIView):
    serializer_class = FactureSerializer

    def get_queryset(self):
        # Récupérer le client spécifié par l'ID dans les paramètres de requête
        client_id = self.kwargs['client_id']
        return Facture.objects.filter(client_id=client_id)
    
