from rest_framework import serializers
from .models import FactureVente

class FactureVenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactureVente
        fields = ['facture_id', 'date_creation', 'date_comptabilisation', 'date_decheance']
