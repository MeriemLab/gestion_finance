from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Devise
from .serializers import DeviseSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework import status
from rest_framework import generics

class DeviseListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Devise.objects.all()
    serializer_class = DeviseSerializer

class DeviseDetailView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Devise.objects.all()
    serializer_class = DeviseSerializer
    
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class DeviseDetailView(RetrieveAPIView):
#     queryset = Devise.objects.all()
#     serializer_class = DeviseSerializer
#     lookup_field = 'pk' 

class DeviseCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Devise.objects.all()
    serializer_class = DeviseSerializer
    

class DeviseUpdateView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Devise.objects.all()
    serializer_class = DeviseSerializer
    lookup_field = 'pk'

class DeviseDeleteView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Devise.objects.all()
    serializer_class = DeviseSerializer
    lookup_field = 'pk'