from rest_framework import serializers
from .models import Factureservice

class FactureserviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factureservice
        fields = ['facture_id', 'date_creation', 'date_comptabilisation', 'date_decheance']
