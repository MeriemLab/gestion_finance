# Generated by Django 5.0.3 on 2024-03-31 14:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factureservice',
            fields=[
                ('date_creation', models.DateField(default=django.utils.timezone.now)),
                ('date_comptabilisation', models.DateField(blank=True, null=True)),
                ('date_decheance', models.DateField(blank=True, null=True)),
                ('facture_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
            ],
        ),
    ]