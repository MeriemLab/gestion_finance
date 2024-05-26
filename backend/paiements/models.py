from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from factures.models import Facture
from devises.models import Devise

class Paiement(models.Model):
    id_paiement = models.AutoField(primary_key=True)
    date_paiement = models.DateField(auto_now_add=True)
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    creer_par = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True , related_name='paiement')
    est_annule = models.BooleanField(default=False)
    Etat_CHOICES=(
        ('complet', 'Complet'),
        ('partiel', 'Partiel'),
    )
    etat = models.CharField(max_length=20, choices=Etat_CHOICES, default='complet')
    Mode_reglement_CHOICES = (
        ('Espèce', 'Espèce'),
        ('Chèque', 'Chèque'),
        ('CIB', 'CIB'),
        ('Avance', 'Avance'),
        ('Virement', 'Virement'),
    )
    mode_reglement = models.CharField(max_length=20, choices=Mode_reglement_CHOICES, default='complet')
    devise = models.ForeignKey(Devise, on_delete=models.CASCADE)
    commentaire = models.CharField(max_length=255)

    def clean(self):
        if self.facture.non_payee == False:
            raise ValidationError(_('La facture associée doit être non payée.'))

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

# class HistoriquePaiement(models.Model):
#     paiement = models.ForeignKey(Paiement, on_delete=models.CASCADE, related_name='historique')
#     Status_CHOICES = (
#         ('annule', 'Annulé'),
#         ('modifie', 'Modifié'),
#         ('autre', 'Autre'),
#     )
#     Status = models.CharField(max_length=20, choices=Status_CHOICES)
#     # Utilisateur = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='operations_paiement')
#     date_operation = models.DateTimeField(auto_now_add=True)
#     raison_annulation = models.TextField(blank=True)