from django.urls import path
from apps.pets import views

app_name = 'pets'
urlpatterns = [
    path('', views.PetListView.as_view(), name='list'),
    path('create/', views.PetCreateView.as_view(), name='create'),
    path('<int:pk>/update/', views.PetUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.PetDeleteView.as_view(), name='delete'),
    path('<int:pk>/profile/', views.PetProfileView.as_view(), name='profile'),
]