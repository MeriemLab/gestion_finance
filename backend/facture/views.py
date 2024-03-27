from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .models import Facture
from .serializers import factureSerializer

class factureListView(ListAPIView):
    queryset = Facture.objects.all()
    serializer_class = factureSerializer

class factureDetailView(RetrieveAPIView):
    queryset = Facture.objects.all()
    serializer_class = factureSerializer
    lookup_field = 'pk'  # Champ utilisÃ© pour la recherche par ID

class factureCreateView(CreateAPIView):
    queryset = Facture.objects.all()
    serializer_class = factureSerializer

class factureUpdateView(UpdateAPIView):
    queryset = Facture.objects.all()
    serializer_class = factureSerializer
    lookup_field = 'pk'

class factureDeleteView(DestroyAPIView):
    queryset =Facture.objects.all()
    serializer_class = factureSerializer
    lookup_field = 'pk'