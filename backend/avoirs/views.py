from rest_framework.generics import RetrieveAPIView, UpdateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework import status
from .models import Avoir
from .serializers import AvoirSerializer, AvoirDetailSerializer
from factures.models import Facture
from django.http import Http404

class AvoirDetailAndCreateAPIView(RetrieveAPIView, UpdateAPIView):
    queryset = Avoir.objects.all()
    serializer_class_detail = AvoirDetailSerializer
    serializer_class_create = AvoirSerializer

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return self.serializer_class_create
        return self.serializer_class_detail

    def get_facture_info(self, facture_id):
        try:
            return Facture.objects.get(pk=facture_id)
        except Facture.DoesNotExist:
            raise Http404("La facture demandée n'existe pas.")


    def get_avoir(self, facture):
        return Avoir.objects.filter(facture=facture)

    def get(self, request, *args, **kwargs):
        facture_id = self.kwargs.get('pk')
        facture = self.get_facture_info(facture_id)

        # Retournez toujours un serializer pré-rempli avec les informations de cette facture
        serializer = self.serializer_class_create(facture)
        return Response(serializer.data)
    def put(self, request, *args, **kwargs):
        facture_id = self.kwargs.get('pk')
        facture = self.get_facture_info(facture_id)
        
        # Valider les données de l'avoir
        serializer = self.serializer_class_create(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Extraire les données validées
        validated_data = serializer.validated_data

        # Créer l'avoir en utilisant les objets associés et les données validées
        avoir = Avoir.objects.create(
            facture=facture,
            client=facture.client,
            commande_ligne=facture.commande_ligne,
            type_facture=validated_data.get('type_facture'),
            avoir_id=validated_data.get('avoir_id'),
            date_comptabilisation=validated_data.get('date_comptabilisation'),
            date_decheance=validated_data.get('date_decheance'),
            non_payee=validated_data.get('non_payee'),
            montant=validated_data.get('montant')
        )
        
        return Response(AvoirSerializer(avoir).data, status=status.HTTP_201_CREATED)    
class AvoirListAPIView(ListAPIView):
    queryset = Avoir.objects.all()
    serializer_class = AvoirSerializer

class AvoirVenteListAPIView(ListAPIView):
    serializer_class = AvoirSerializer

    def get_queryset(self):
        return Avoir.objects.filter(type_facture='Vente')

class AvoirServiceListAPIView(ListAPIView):
    serializer_class = AvoirSerializer

    def get_queryset(self):
        return Avoir.objects.filter(type_facture='Service')