from apps.accounts.models import Profile
from datetime import date
from django.db import models
from django.utils import timezone
from shared.models import BaseModel


class Pet(BaseModel):
    class Species(models.TextChoices):
        DOG = 'DOG', 'Cachorro'
        CAT = 'CAT', 'Gato'
    
    class Status(models.TextChoices):
        ALIVE = 'alive', 'Vivo'
        DECEASE = 'decease', 'Falecido'
    
    tutor = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='pets')
    name = models.CharField('Nome do pet', max_length=100)
    species = models.CharField('Espécie', max_length=20, choices=Species.choices)
    breed = models.CharField('Raça', max_length=100, blank=True)
    birth_date = models.DateField('Data de nascimento', null=True, blank=True)
    status = models.CharField(
        'Status',
        max_length=10,
        choices=Status.choices,
        default=Status.ALIVE
    )
    decease_date = models.DateField(
        'Data de falecimento',
        blank=True,
        null=True,
    )
    homage_message = models.TextField(
        'Mensagem de homenagem',
        help_text='Uma mensagem ou memória especial para homenagear o pet.',
        blank=True,
        null=True
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Pet'
        verbose_name_plural = 'Pets'

    def __str__(self):
        return f'{self.name} ({self.get_species_display()})'
    
    def mark_as_deceased(self, decease_date=None, message=None):
        """
        Altera o status do animal para 'deceased'.
        Salva a data de falecimento e a mensagem de homenagem.

        TODO: Gerar uma mensagem de despedida com IA.
        """
        if self.status == self.Status.ALIVE:
            self.status = self.Status.DECEASE
            self.decease_date = decease_date if decease_date else timezone.now().date()
            self.homage_message = message
            self.save()
            return True
        return False
    
    @property
    def age(self):
        if not self.birth_date:
            return None

        today = date.today()
        years = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))

        if years > 0:
            return f"{years} ano{'s' if years > 1 else ''}"
        else:
            months = (today.year - self.birth_date.year) * 12 + today.month - self.birth_date.month
            if today.day < self.birth_date.day:
                months -= 1
            
            if months <= 0:
                return "Menos de 1 mês"
            
            return f"{months} mes{'es' if months > 1 else ''}"
