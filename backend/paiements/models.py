from django.db import models
from django.utils import timezone

class FactureVente(models.Model):
    numero = models.CharField(max_length=20)
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)

class FactureService(models.Model):
    numero = models.CharField(max_length=20)
    montant_total = models.DecimalField(max_digits=10, decimal_places=2)

class Paiement(models.Model):
    facture_vente = models.ForeignKey(FactureVente, on_delete=models.CASCADE)
    facture_service = models.ForeignKey(FactureService, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement = models.DateField(default=timezone.now)
