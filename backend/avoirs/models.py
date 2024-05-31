from django.db import models
from django.utils import timezone
from factures.models import Facture
from clients.models import Client
from commandes.models import Commande_ligne

class Avoir(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, related_name='avoirs', null=True, blank=True)
    TYPE_CHOICES = [
        ('Vente', 'Vente'),
        ('Service', 'Service'),
    ]

    type_facture = models.CharField(max_length=10, choices=TYPE_CHOICES)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='avoir_ids_avoir')
    commande_ligne = models.ForeignKey(Commande_ligne, on_delete=models.CASCADE, related_name='avoir_ids_avoir')
    avoir_id = models.CharField(max_length=20, unique=True, editable=False)
    date_creation = models.DateField(auto_now_add=True)
    date_comptabilisation = models.DateField(null=True, blank=True)
    date_decheance = models.DateField(null=True, blank=True)
    non_payee = models.BooleanField(default=False)
    montant = models.DecimalField(max_digits=10, decimal_places=2, default="0")
    
    def generate_id(self):
        current_year = timezone.now().strftime('%Y')
        last_avoir_number = self.get_last_invoice_number() + 1
        prefix = 'A' 
        return f"{prefix}{current_year}{last_avoir_number:04d}"

    @classmethod
    def get_last_invoice_number(cls):
        last_invoice = cls.objects.order_by('-id').first()
        if last_invoice:
            return int(last_invoice.avoir_id[6:])
        return 0
    
    def save(self, *args, **kwargs):
        if not self.avoir_id:
            self.avoir_id = self.generate_id()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"avoir_id {self.avoir_id}"