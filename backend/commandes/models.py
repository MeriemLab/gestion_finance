from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from clients.models import Client
from produits.models import Produit



   
class Commande(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    
    produits = models.ManyToManyField(Produit, through='commande_ligne')

   #prix_unitaire = models.DecimalField(max_digits=10, decimal_places=2)
    #quantite = models.IntegerField()
    date_commande=models.DateField()
    pht = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tva = models.DecimalField(max_digits=5, decimal_places=2)
    mtva = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    tht = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ttva = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    ttc = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    est_promo = models.BooleanField(default=False)
    code_promo = models.CharField(max_length=50, blank=True, null=True)
    

@receiver(pre_save, sender=Commande)
def update_fields(sender, instance, **kwargs):
    if instance.pht is not None and instance.tva is not None:
        instance.mtva = instance.pht * instance.tva / 100
    else:
        instance.mtva = None
    instance.tht = instance.pht
    instance.ttva = instance.mtva

    
class Commande_ligne(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)  
    produits = models.ForeignKey(Produit, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)  
    class Meta:
        unique_together = (('commande', 'produits'),)