from rest_framework import serializers
from .models import FactureService
from .models import FactureVente
class FactureServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactureService
        fields = '__all__'
class FactureVenteSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactureVente
        fields = '__all__'