# pets/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.pets.models import Pet
from apps.pets.forms import PetForm

class PetListView(LoginRequiredMixin, ListView):
    model = Pet
    template_name = 'pets/pet_list.html'
    context_object_name = 'pets'

    def get_queryset(self):
        # Filtra os pets para mostrar apenas os do tutor logado
        return Pet.objects.filter(tutor=self.request.user.profile)

class PetCreateView(LoginRequiredMixin, CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet_form.html'
    success_url = reverse_lazy('pets:list')

    def form_valid(self, form):
        # Associa o pet ao perfil do tutor logado antes de salvar
        form.instance.tutor = self.request.user.profile
        return super().form_valid(form)

class PetUpdateView(LoginRequiredMixin, UpdateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet_form.html'
    success_url = reverse_lazy('pets:list')

    def get_queryset(self):
        # Garante que o usuário só pode editar seus próprios pets
        return Pet.objects.filter(tutor=self.request.user.profile)

class PetDeleteView(LoginRequiredMixin, DeleteView):
    model = Pet
    template_name = 'pets/pet_confirm_delete.html'
    success_url = reverse_lazy('pets:list')
    context_object_name = 'pet'

    def get_queryset(self):
        # Garante que o usuário só pode deletar seus próprios pets
        return Pet.objects.filter(tutor=self.request.user.profile)