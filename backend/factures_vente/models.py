from django.db import models
from django.utils import timezone

class FactureVente(models.Model):
    id = models.AutoField(primary_key=True)
    facture_id = models.CharField(max_length=20, unique=True , editable=False)
    date_creation = models.DateField(auto_now_add=True)
    date_comptabilisation = models.DateField(null=True, blank=True)
    date_decheance = models.DateField(null=True, blank=True)
    # Champ facture_id comme cle primaire

    def generate_id(self):
        return f"F{timezone.now().strftime('%Y%m%d')}"

    def save(self, *args, **kwargs):
        if not self.facture_id:
            self.facture_id = self.generate_id()
        super().save(*args, **kwargs)