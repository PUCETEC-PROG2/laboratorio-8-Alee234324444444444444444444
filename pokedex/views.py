from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from pokedex.forms import PokemonForm, TrainerForm
from .models import Pokemon, Trainer
from django.contrib.auth.views import LoginView

def index(request):
    pokemons = Pokemon.objects.order_by('type')
    return render(request, 'index.html', {'pokemons': pokemons})

def pokemon(request, pokemon_id):
    pokemon = get_object_or_404(Pokemon, pk=pokemon_id)
    return render(request, 'display_pokemon.html', {'pokemon': pokemon})

@login_required
def add_pokemon(request):
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm()
    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def edit_pokemon(request, id):
    pokemon = get_object_or_404(Pokemon, pk=id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect('pokedex:index')
    else:
        form = PokemonForm(instance=pokemon)
    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def delete_pokemon(request, id):
    pokemon = get_object_or_404(Pokemon, pk=id)
    pokemon.delete()
    return redirect('pokedex:index')

@login_required
def trainers_list(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainers_list.html', {'trainers': trainers})

def trainer(request, trainer_id):
    trainer = get_object_or_404(Trainer, pk=trainer_id)
    return render(request, 'display_trainer.html', {'trainer': trainer})

@login_required
def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pokedex:trainers_list')
    else:
        form = TrainerForm()
    return render(request, 'trainer_form.html', {'form': form})

@login_required
def edit_trainer(request, id):
    trainer = get_object_or_404(Trainer, pk=id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, request.FILES, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('pokedex:trainers_list')
    else:
        form = TrainerForm(instance=trainer)
    return render(request, 'trainer_form.html', {'form': form})

@login_required
def delete_trainer(request, id):
    trainer = get_object_or_404(Trainer, pk=id)
    trainer.delete()
    return redirect('pokedex:trainers_list')

class CustomLoginView(LoginView):
    template_name = 'login.html'
