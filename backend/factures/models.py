from django.db import models
from django.utils import timezone
from clients.models import Client
from commandes.models import Commande_ligne

class FactureService(models.Model):
    id = models.AutoField(primary_key=True)
    commande_ligne = models.ForeignKey(Commande_ligne, on_delete=models.CASCADE, related_name='facture_services')  
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='facture_services')

    facture_id = models.CharField(max_length=20, unique=True, editable=False)
    date_creation = models.DateField(auto_now_add=True)
    date_comptabilisation = models.DateField(null=True, blank=True)
    date_decheance = models.DateField(null=True, blank=True)
    non_payée = models.BooleanField(default=False) 

    @classmethod
    def get_last_invoice_number(cls):
        last_invoice = cls.objects.order_by('-id').first()
        if last_invoice:
            return int(last_invoice.facture_id[5:])  
        return 0

    def generate_id(self):
        current_year = timezone.now().strftime('%Y')
        last_invoice_number = self.get_last_invoice_number() + 1
        return f"FA{current_year}{last_invoice_number:04d}"  

    def save(self, *args, **kwargs):
        if not self.facture_id:
            self.facture_id = self.generate_id()
        super().save(*args, **kwargs)
class FactureVente(models.Model):
    id = models.AutoField(primary_key=True)
    commande_ligne = models.ForeignKey(Commande_ligne, on_delete=models.CASCADE, related_name='facture_ventes') 
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='facture_ventes')
    facture_id = models.CharField(max_length=20, unique=True, editable=False)
    date_creation = models.DateField(auto_now_add=True)
    date_comptabilisation = models.DateField(null=True, blank=True)
    date_decheance = models.DateField(null=True, blank=True)
    non_payée = models.BooleanField(default=False) 
    @classmethod
    def get_last_invoice_number(cls):
        last_invoice = cls.objects.order_by('-id').first()
        if last_invoice:
            return int(last_invoice.facture_id[5:]) 
        return 0

    def generate_id(self):
        current_year = timezone.now().strftime('%Y')
        last_invoice_number = self.get_last_invoice_number() + 1
        return f"F{current_year}{last_invoice_number:04d}"  

    def save(self, *args, **kwargs):
        if not self.facture_id:
            self.facture_id = self.generate_id()
        super().save(*args, **kwargs)
