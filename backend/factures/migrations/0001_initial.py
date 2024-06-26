# Generated by Django 5.0.4 on 2024-05-05 20:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clients', '0007_client_dossier_valide_and_more'),
        ('commandes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_facture', models.CharField(choices=[('Vente', 'Vente'), ('Service', 'Service')], max_length=10)),
                ('facture_id', models.CharField(editable=False, max_length=20, unique=True)),
                ('date_creation', models.DateField(auto_now_add=True)),
                ('date_comptabilisation', models.DateField(blank=True, null=True)),
                ('date_decheance', models.DateField(blank=True, null=True)),
                ('non_payee', models.BooleanField(default=False)),
                ('montant', models.DecimalField(decimal_places=2, default='0', max_digits=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factures', to='clients.client')),
                ('commande_ligne', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='factures', to='commandes.commande_ligne')),
            ],
        ),
    ]
