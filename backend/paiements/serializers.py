from rest_framework import serializers
from .models import Paiement

class PaiementSerializer(serializers.ModelSerializer):
    cree_par = serializers.ReadOnlyField(source='cree_par.username')
    class Meta:
        model = Paiement
        fields = '__all__'
        