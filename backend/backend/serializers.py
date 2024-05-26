from rest_framework import serializers
from django.utils.html import escape
from clients.models import Client
class CustomSerializer(serializers.ModelSerializer):
    field_name = serializers.CharField()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        # Échapper les données ici si nécessaire
        data['field_name'] = escape(data['field_name'])
        return data

    class Meta:
        model = Client
        fields = ['field_name']
