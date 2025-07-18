# Generated by Django 5.2.4 on 2025-07-17 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pet',
            name='decease_date',
            field=models.DateField(blank=True, null=True, verbose_name='Data de falecimento'),
        ),
        migrations.AddField(
            model_name='pet',
            name='homage_message',
            field=models.TextField(blank=True, help_text='Uma mensagem ou memória especial para homenagear o pet.', null=True, verbose_name='Mensagem de homenagem'),
        ),
        migrations.AddField(
            model_name='pet',
            name='status',
            field=models.CharField(choices=[('alive', 'Vivo'), ('decease', 'Falecido')], default='alive', max_length=10, verbose_name='Status'),
        ),
    ]
