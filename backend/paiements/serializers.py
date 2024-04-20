from rest_framework import serializers
from .models import FactureVente, FactureService, Paiement

class FactureVenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactureVente
        fields = '__all__'

class FactureServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactureService
        fields = '__all__'

class PaiementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paiement
        fields = '__all__'
