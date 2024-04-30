import io
from rest_framework.permissions import IsAuthenticated
from .models import FactureService
from .serializers import FactureServiceSerializer
from rest_framework.generics import ListAPIView,  CreateAPIView, UpdateAPIView 
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter , A4
from reportlab.platypus import Table
from reportlab.lib import colors
from django.views.generic import View
from django.http import  HttpResponse
from .models import FactureVente
from .serializers import FactureVenteSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

class FactureServiceListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FactureService.objects.all()
    serializer_class = FactureServiceSerializer

class FactureServiceCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FactureService.objects.all()
    serializer_class = FactureServiceSerializer

class FactureServiceUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FactureService.objects.all()
    serializer_class = FactureServiceSerializer

class PDFFactureView(View):
    def get(self, requNon, id, *args, **kwargs):
     try:
        facture = FactureService.objects.get(id=id)

        buffer = io.BytesIO()

        pdf = canvas.Canvas(buffer)

        pdf.drawString(100, 740, f"ID Facture: {facture.facture_id}")
        pdf.drawString(100, 800, f"Date de création: {facture.date_creation}")
        pdf.drawString(100, 780, f"Date de comptabilisation: {facture.date_comptabilisation}")
        pdf.drawString(100, 760, f"Date de déchéance: {facture.date_decheance}")
        
        pdf.showPage()
        pdf.save()

        pdf_data = buffer.getvalue()

        response = HttpResponse(pdf_data, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="facture.pdf"'
        # pour le téléchargement automatique
        #response['Content-Disposition'] = f'attachment; filename="facture_{id}.pdf"'

        return response
     except FactureService.DoesNotExist:
        return HttpResponse('La facture demandée n\'existe pas.', status=404)



class FactureVenteListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FactureVente.objects.all()
    serializer_class = FactureVenteSerializer

class FactureVenteCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FactureVente.objects.all()
    serializer_class = FactureVenteSerializer

class FactureVenteUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = FactureVente.objects.all()
    serializer_class = FactureVenteSerializer

class VueListeNonpayée(generics.ListAPIView):
    serializer_class = FactureVenteSerializer

    def get_queryset(self):
        return FactureVente.objects.filter(non_payée=True)
    
class VueListeNonpayée(APIView):
    def get(self, request, format=None):
        factures_service = FactureService.objects.filter(non_payée=True)
        factures_vente = FactureVente.objects.filter(non_payée=True)

        factures_service_serialized = FactureServiceSerializer(factures_service, many=True)
        factures_vente_serialized = FactureVenteSerializer(factures_vente, many=True)

        return Response({
            "factures_service": factures_service_serialized.data,
            "factures_vente": factures_vente_serialized.data
        })