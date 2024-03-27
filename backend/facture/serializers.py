from rest_framework import serializers
from .models import Facture

class factureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facture
        fields = '__all__'