import io
from .models import FactureVente
from .serializers import FactureVenteSerializer
from rest_framework.generics import ListAPIView,  CreateAPIView, UpdateAPIView 
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter , A4
from reportlab.platypus import Table, TableStyle
from reportlab.lib import colors
from django.views.generic import View
from django.http import  HttpResponse

class FactureVenteListView(ListAPIView):
    queryset = FactureVente.objects.all()
    serializer_class = FactureVenteSerializer

class FactureVenteCreateView(CreateAPIView):
    queryset = FactureVente.objects.all()
    serializer_class = FactureVenteSerializer

class FactureVenteUpdateView(UpdateAPIView):
    queryset = FactureVente.objects.all()
    serializer_class = FactureVenteSerializer

class PDFFactureView(View):
    def get(self, request, id, *args, **kwargs):
     try:
        facture = FactureVente.objects.get(id=id)

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
     except FactureVente.DoesNotExist:
        return HttpResponse('La facture demandée n\'existe pas.', status=404)
