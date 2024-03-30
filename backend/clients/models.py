from django.db import models

class Client(models.Model):
    
    etat_dossier = (
        ('Y', ('Yes')),
        ('N', ('No')),
    )

    etat_statut= (
        ('A', ('Active')),
        ('I', ('Inactive')),
    )

    categorie = (
        ('C', ('Client')),
        ('S', ('Supplier')),
    )
    dossier_valide=(
        ('t', ('true')),
        ('f', ('false')),
     )

    id = models.CharField(max_length=100 , primary_key=True,blank=True)

    categorie_compte  = models.CharField(max_length=10, choices=categorie,blank=True)

    raison_sociale = models.CharField(max_length=64,blank=True)

    sigle = models.CharField(max_length=64,blank=True)

    code_tva = models.CharField(max_length=100,blank=True)

    nature_compte = models.CharField(max_length=100,blank=True)

    nif = models.CharField(max_length=100,blank=True)

    nis = models.CharField(max_length=100,blank=True)

    registre_commerce = models.CharField(max_length=100,blank=True)

    article_imposition = models.CharField(max_length=100,blank=True)

    devise = models.CharField(max_length=100,blank=True)

    rue = models.CharField(max_length=100,blank=True)

    ville = models.CharField(max_length=100,blank=True)  

    region = models.CharField(max_length=100,blank=True)

    type_de_region = models.CharField(max_length=100,blank=True)

    code_postale = models.CharField(max_length=100,blank=True)

    pays = models.CharField(max_length=100,blank=True)

    telephone = models.CharField(max_length=100,blank=False)

    email = models.EmailField(blank=False)

    secteur_activite = models.CharField(max_length=100,blank=True)

    condition_paiement = models.CharField(max_length=100,blank=True)

    cree_le = models.DateTimeField(auto_now_add=True,blank=True)

    cree_par =  models.CharField(max_length=100,blank=True)

    nom = models.CharField(max_length=100,blank=False)

    prenom = models.CharField(max_length=100,blank=False)

    fonction = models.CharField(max_length=100 ,blank=True)

    type_client = models.CharField(max_length=100,blank=True)

    fax = models.CharField(max_length=100,blank=True)

    #dossier_valide = models.CharField(max_length=1, choices=etat_dossier,blank=True)

    statut = models.CharField(max_length=1, choices=etat_statut,blank=True)
    est_vip = models.BooleanField(default=False) 
    class Meta: 
        verbose_name = "client"
        verbose_name_plural = "clients"

    def __str__(self):
        return self.name