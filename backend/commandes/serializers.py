from rest_framework import serializers
from .models import Commande,Commande_ligne


class CommandeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande
        fields = '__all__'
class Commande_ligneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Commande_ligne
        fields = '__all__'