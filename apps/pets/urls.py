from django.urls import path
from apps.pets.views import (
    pet_views, exam_views
)

app_name = 'pets'
urlpatterns = [
    path('', pet_views.PetListView.as_view(), name='list'),
    path('create/', pet_views.PetCreateView.as_view(), name='create'),
    path('<int:pk>/update/', pet_views.PetUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', pet_views.PetDeleteView.as_view(), name='delete'),
    path('<int:pk>/profile/', pet_views.PetProfileView.as_view(), name='profile'),
]