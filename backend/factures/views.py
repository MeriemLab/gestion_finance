from django.shortcuts import render
from rest_framework.generics import ListAPIView,  CreateAPIView, RetrieveAPIView
from rest_framework import generics
from .models import Facture
from .serializers import FactureSerializer , FactureAjoutSerializer
from django.http import HttpResponse
from reportlab.pdfgen import canvas
from commandes.models import Commande
from commandes.models import Commande_ligne
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter , A4
from django.views.generic import View
from django.http import  HttpResponse
from .models import Facture
from .serializers import FactureSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from io import BytesIO
from decimal import Decimal
from avoirs.serializers import AvoirSerializer
from avoirs.models import Avoir


class PDFFactureView(View):
    def get(self, request, id, *args, **kwargs):
        try:
            facture = Facture.objects.get(id=id)
            commande_lignes = facture.commande_ligne.all()

            buffer = BytesIO()

            pdf = canvas.Canvas(buffer, pagesize=A4)
            
            pdf.drawString(25, 800, f"ID Facture: {facture.facture_id}")
            pdf.drawString(25, 780, f"Client: {facture.client.nom}")
            pdf.drawString(25, 760, f"Date de création: {facture.date_creation}")
            pdf.drawString(25, 740, f"Date de comptabilisation: {facture.date_comptabilisation}")
            pdf.drawString(25, 720, f"Date de déchéance: {facture.date_decheance}")

           
            pdf.drawString(25, 660, "Produit")
            pdf.drawString(115, 660, "Prix unitaire")
            pdf.drawString(205, 660, "Quantité")
            pdf.drawString(295,660,"TVA")
            pdf.drawString(385, 660, "PHT")
            pdf.drawString(475, 660, "PTC") 

            
            y_position = 630
            total_pht = Decimal('0')

             
            for commande_ligne in commande_lignes:
                produit = commande_ligne.produit
                commande = commande_ligne.commande

                pdf.drawString(20, y_position, produit.nom)
                pdf.drawString(125, y_position, f"{produit.prix_unitaire:.2f} ")
                pdf.drawString(230, y_position, str(commande_ligne.quantity))
                pdf.drawString(295, y_position, f"{facture.client.code_tva}%")
                pdf.drawString(380, y_position, f"{commande.pht:.2f} ")
                pdf.drawString(470, y_position, f"{commande.ttc:.2f} ")

                total_pht += Decimal(commande.pht)
                y_position -= 20  

            pdf.drawString(385, y_position-10, "THT:")
            pdf.drawString(385, y_position-25, "TVA:  ")
            pdf.drawString(385, y_position-40, "TTC: ")

            pdf.drawString(420, y_position-10, f" {total_pht:.2f} {facture.client.devise} ")
            pdf.drawString(420, y_position-25, f" {total_pht * Decimal(facture.client.code_tva) / Decimal('100'):.2f} {facture.client.devise} ")
            pdf.drawString(420, y_position-40, f" {total_pht + (total_pht * Decimal(facture.client.code_tva) / Decimal('100')):.2f} {facture.client.devise} ")
              
            pdf.showPage()
            pdf.save()

            pdf_data = buffer.getvalue()

            response = HttpResponse(pdf_data, content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="facture.pdf"'
            # pour le téléchargement automatique
            #response['Content-Disposition'] = f'attachment; filename="facture_{id}.pdf"'

            return response
        except Facture.DoesNotExist:
            return HttpResponse('La facture demandée n\'existe pas.', status=404)


class FactureListView(ListAPIView):
    
    queryset = Facture.objects.all()
    serializer_class = FactureSerializer

# class FactureDetail(RetrieveAPIView):
#     queryset = Facture.objects.all()
#     serializer_class = FactureSerializer
#     lookup_field = 'id'

class FactureListCreate(CreateAPIView):
    queryset = Facture.objects.all()
    serializer_class = FactureAjoutSerializer


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

class AvoirsFacturesAPIView(ListAPIView):
    serializer_class = AvoirSerializer

    def get_queryset(self):
        # Récupérer l'ID de la facture spécifié dans les paramètres de requête
        id = self.kwargs['id']
        # Filtrer les avoirs en fonction de l'ID de la facture
        return Avoir.objects.filter(facture_id=id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data)
        else:
            # Gérer le cas où aucun avoir n'est trouvé pour la facture
            return Response({"detail": "Aucun avoir trouvé pour cette facture."}, status=status.HTTP_404_NOT_FOUND)