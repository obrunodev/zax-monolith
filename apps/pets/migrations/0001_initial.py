# Generated by Django 5.2.4 on 2025-07-16 03:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
                ('name', models.CharField(max_length=100, verbose_name='Nome do pet')),
                ('species', models.CharField(choices=[('DOG', 'Cachorro'), ('CAT', 'Gato')], max_length=20, verbose_name='Espécie')),
                ('breed', models.CharField(blank=True, max_length=100, verbose_name='Raça')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Data de nascimento')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='accounts.profile')),
            ],
            options={
                'verbose_name': 'Pet',
                'verbose_name_plural': 'Pets',
                'ordering': ['name'],
            },
        ),
    ]
