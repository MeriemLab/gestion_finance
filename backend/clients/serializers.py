from rest_framework import serializers
from .models import Client

class ClientSerializer(serializers.ModelSerializer):
    devise_nom = serializers.SerializerMethodField()  

    class Meta:
        model = Client
        fields = '__all__'

    def get_devise_nom(self, obj):
        if obj.devise:
            return obj.devise.devise
        return None
