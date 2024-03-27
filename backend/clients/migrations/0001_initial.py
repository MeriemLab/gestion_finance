# Generated by Django 5.0.3 on 2024-03-22 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('categorie_compte', models.CharField(choices=[('C', 'Client'), ('S', 'Supplier')], max_length=10)),
                ('raison_sociale', models.CharField(max_length=64)),
                ('sigle', models.CharField(max_length=64)),
                ('code_tva', models.CharField(max_length=100)),
                ('nature_compte', models.CharField(max_length=100)),
                ('nif', models.CharField(max_length=100)),
                ('nis', models.CharField(max_length=100)),
                ('registre_commerce', models.CharField(max_length=100)),
                ('article_imposition', models.CharField(max_length=100)),
                ('devise', models.CharField(max_length=100)),
                ('rue', models.CharField(max_length=100)),
                ('ville', models.CharField(max_length=100)),
                ('region', models.CharField(max_length=100)),
                ('type_de_region', models.CharField(max_length=100)),
                ('code_postale', models.CharField(max_length=100)),
                ('pays', models.CharField(max_length=100)),
                ('telephone', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('secteur_activite', models.CharField(max_length=100)),
                ('condition_paiement', models.CharField(max_length=100)),
                ('cree_le', models.DateTimeField(auto_now_add=True)),
                ('cree_par', models.CharField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('fonction', models.CharField(max_length=100)),
                ('type_client', models.CharField(max_length=100)),
                ('fax', models.CharField(max_length=100)),
                ('dossier_valide', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], max_length=1)),
                ('statut', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive')], max_length=1)),
            ],
            options={
                'verbose_name': 'client',
                'verbose_name_plural': 'clients',
            },
        ),
    ]
