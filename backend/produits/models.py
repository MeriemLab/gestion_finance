from django.db import models



class Produit(models.Model):

  nom = models.CharField(max_length=100, blank=False)
  prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
  description =   models.CharField(max_length=100, blank=False)
  def __str__(self):
        return self.nom