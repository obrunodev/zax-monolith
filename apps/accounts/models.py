from django.contrib.auth.models import User
from django.db import models
from shared.models import BaseModel


class Profile(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    phone_number = models.CharField('Telefone', max_length=20, blank=True, null=True)
    address = models.CharField('Endereço', max_length=255, blank=True, null=True)

    # --- Se necessário implementar ROLE, adicionar campo aqui ---

    class Meta:
        ordering = ['user']
        verbose_name = 'Perfil do usuário'
        verbose_name_plural = 'Perfis do usuário'

    def __str__(self):
        return f'{self.user.username}'
