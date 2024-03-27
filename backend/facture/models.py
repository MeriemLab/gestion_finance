
from django.db import models

class Facture(models.Model):
   # id = models.CharField(max_length=100 , primary_key=True)
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    paiement = models.CharField(max_length=100)
    code_tva = models.CharField(max_length=100)

    class Meta: 
        verbose_name = "facture"
        verbose_name_plural = "factures"

    def str(self):
        return f"{self.nom} {self.prenom} - {self.code_tva}" 
