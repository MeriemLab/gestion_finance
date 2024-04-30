from rest_framework import serializers
from .models import Produit

class ProduitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = '__all__'

    def create(self, validated_data):
        return Produit.objects.create(**validated_data)
