from django.db import models
from django.utils import timezone

class Factureservice(models.Model):
    date_creation = models.DateField(default=timezone.now)
    date_comptabilisation = models.DateField(null=True, blank=True)
    date_decheance = models.DateField(null=True, blank=True)
    facture_id = models.CharField(max_length=20, primary_key=True)  

    def generate_id(self):
        return f"F{self.date_creation.strftime('%Y%m%d')}"

    def save(self, *args, **kwargs):
        if not self.facture_id:
            self.facture_id = self.generate_id()
        super().save(*args, **kwargs)
