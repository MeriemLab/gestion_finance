from rest_framework import serializers
from .models import Avoir
from clients.serializers import InfoClientSerializer

class AvoirSerializer(serializers.ModelSerializer):
    client = InfoClientSerializer()
    
    class Meta:
        model = Avoir
        fields = '__all__'

class AvoirDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avoir
        fields = '__all__'
