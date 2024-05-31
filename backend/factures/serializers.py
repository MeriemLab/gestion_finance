from rest_framework import serializers

from clients.serializers import InfoClientSerializer 
from .models import Facture

class FactureSerializer(serializers.ModelSerializer): 
    client = InfoClientSerializer()
    
    class Meta:
        model = Facture
        fields = '__all__'


class FactureAjoutSerializer(serializers.ModelSerializer): 
    class Meta:
        model = Facture
        fields = '__all__'