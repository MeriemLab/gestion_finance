from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from .models import Paiement
from .serializers import PaiementSerializer
from factures.models import Facture
from rest_framework.views import APIView

class ListePaiements(generics.ListAPIView):
    queryset = Paiement.objects.all()
    serializer_class = PaiementSerializer

class PaiementCreateView(APIView):
    def post(self, request, pk):
        facture = get_object_or_404(Facture, pk=pk, non_payee=True)
        montant = facture.montant  # Récupérer le montant de la facture
        devise = facture.client.devise  # Récupérer la devise du client associé à la facture
        creer_par = request.user  # Utilisateur qui crée le paiement
        
        # Récupérer les données de l'utilisateur depuis la requête POST
        etat = request.data.get('etat')
        est_annule = request.data.get('est_annule')
        mode_reglement = request.data.get('mode_reglement')
        commentaire = request.data.get('commentaire')

        paiement = Paiement.objects.create(
            facture=facture,
            montant=montant,
            devise=devise,
            creer_par=creer_par,
            etat=etat,
            est_annule=est_annule,
            mode_reglement=mode_reglement,
            commentaire=commentaire,
        )

        # Marquer la facture comme payée
        facture.non_payee = False
        facture.save()

        serializer = PaiementSerializer(paiement)
        return Response(serializer.data, status=status.HTTP_201_CREATED)