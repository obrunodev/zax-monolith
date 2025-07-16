from apps.accounts.models import Profile
from datetime import date
from django.db import models
from shared.models import BaseModel


class Pet(BaseModel):
    class Species(models.TextChoices):
        DOG = 'DOG', 'Cachorro'
        CAT = 'CAT', 'Gato'
        # Adiciona mais tipos aqui
    
    tutor = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='pets')
    name = models.CharField('Nome do pet', max_length=100)
    species = models.CharField('Espécie', max_length=20, choices=Species.choices)
    breed = models.CharField('Raça', max_length=100, blank=True)
    birth_date = models.DateField('Data de nascimento', null=True, blank=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'

    def __str__(self):
        return f'{self.name} ({self.get_species_display()})'
    
    @property
    def age(self):
        if not self.birth_date:
            return None # Retorna nada se a data de nascimento não for cadastrada

        today = date.today()
        # Calcula a idade em anos
        years = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))

        if years > 0:
            return f"{years} ano{'s' if years > 1 else ''}"
        else:
            # Se tiver menos de 1 ano, calcula em meses
            months = (today.year - self.birth_date.year) * 12 + today.month - self.birth_date.month
            if today.day < self.birth_date.day:
                months -= 1
            
            if months <= 0: # Para pets com menos de 1 mês
                return "Menos de 1 mês"
            
            return f"{months} mes{'es' if months > 1 else ''}"
