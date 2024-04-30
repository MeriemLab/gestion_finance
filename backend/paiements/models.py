from django.db import models
from django.utils import timezone

from factures.models import FactureVente
from factures.models import FactureService

class Paiement(models.Model):
    COMPLET = 'C'
    PARTIEL = 'P'
    TYPE_CHOICES = [
        (COMPLET, 'Complet'),
        (PARTIEL, 'Partiel'),
    ]

    facture_vente = models.ForeignKey(FactureVente, on_delete=models.CASCADE)
    facture_service = models.ForeignKey(FactureService, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_creation = models.DateField(auto_now_add=True)
    type_paiement = models.CharField(max_length=1, choices=TYPE_CHOICES, default=PARTIEL)
