from rest_framework import serializers
from .models import Client
from devises.serializers import DeviseSerializer


class ClientSerializer(serializers.ModelSerializer):
    devise = DeviseSerializer()

    class Meta:
        model = Client
        fields = '__all__'


class InfoClientSerializer(serializers.ModelSerializer):
    devise = DeviseSerializer()
    
    class Meta:
        model = Client
        fields = ['id', 'nom', 'devise' ]

class ClientAjoutSerializer(serializers.ModelSerializer):
  

    class Meta:
        model = Client
        fields = '__all__'


