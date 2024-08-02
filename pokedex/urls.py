from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'pokedex'

urlpatterns = [
    path("", views.index, name="index"),
    path("pokemon/<int:pokemon_id>/", views.pokemon, name="pokemon"),
    path("add_pokemon/", views.add_pokemon, name="add_pokemon"),
    path("edit_pokemon/<int:id>/", views.edit_pokemon, name="edit_pokemon"),
    path("delete_pokemon/<int:id>/", views.delete_pokemon, name="delete_pokemon"),
    path("trainers/", views.trainers_list, name="trainers_list"),
    path("add_trainer/", views.add_trainer, name="add_trainer"),
    path("edit_trainer/<int:id>/", views.edit_trainer, name="edit_trainer"),
    path("delete_trainer/<int:id>/", views.delete_trainer, name="delete_trainer"),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("trainer/<int:trainer_id>/", views.trainer, name="trainer"),
]
