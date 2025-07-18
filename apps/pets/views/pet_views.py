# pets/views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.pets.models import Pet
from apps.pets.forms import PetForm

class PetListView(LoginRequiredMixin, ListView):
    model = Pet
    template_name = 'pets/pet_list.html'
    context_object_name = 'pets'

    def get_queryset(self):
        return Pet.objects.filter(tutor=self.request.user.profile)

class PetCreateView(LoginRequiredMixin, CreateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet_form.html'
    success_url = reverse_lazy('pets:list')

    def form_valid(self, form):
        form.instance.tutor = self.request.user.profile
        return super().form_valid(form)

class PetUpdateView(LoginRequiredMixin, UpdateView):
    model = Pet
    form_class = PetForm
    template_name = 'pets/pet_form.html'
    success_url = reverse_lazy('pets:list')

    def get_queryset(self):
        return Pet.objects.filter(tutor=self.request.user.profile)

class PetDeleteView(LoginRequiredMixin, DeleteView):
    model = Pet
    template_name = 'pets/pet_confirm_delete.html'
    success_url = reverse_lazy('pets:list')
    context_object_name = 'pet'

    def get_queryset(self):
        return Pet.objects.filter(tutor=self.request.user.profile)


class PetProfileView(DetailView):
    model = Pet
    template_name = 'pets/pet_profile.html'
    context_object_name = 'pet'

    def get_queryset(self):
        return super().get_queryset().prefetch_related(
            'exams__results'
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['exams'] = self.object.exams.all()
        return context
