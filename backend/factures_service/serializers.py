from rest_framework import serializers
from .models import FactureService

class FactureServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactureService
        fields = ['facture_id', 'date_creation', 'date_comptabilisation', 'date_decheance']
