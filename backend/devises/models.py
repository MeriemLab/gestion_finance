from django.db import models

class Devise(models.Model):
    EUR = 'EUR'
    GBP = 'GBP'
    USD = 'USD'
    CAD = 'CAD'
    AUD = 'AUD'
    JPY = 'JPY'

    DEVISE_CHOICES = (
        (EUR, 'EUR (EUR)'),
        (GBP, 'GBP (GBP)'),
        (USD, 'USD (USD)'),
        (CAD, 'CAD (CAD)'),
        (AUD, 'AUD (AUD)'),
        (JPY, 'JPY (JPY)'),
    )

    devise = models.CharField(max_length=10, choices=DEVISE_CHOICES ,default=EUR)
    def __str__(self):
        return self.devise