from django.db import models
from . import pokedex
from django.db.models.signals import m2m_changed
from django.core.exceptions import ValidationError

class Pokemon(models.Model):
    # A pokemon name can only be one of the possibilities of the pokemon API
    name = models.CharField(max_length = 30, choices = pokedex.CHOICES)

    def __str__(self):
        return self.name

class Trainer(models.Model):
    name = models.CharField(max_length=30)

    # To be able to register a trainer with its name when creating a team
    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length = 20)
    trainer = models.ForeignKey(Trainer, on_delete = models.CASCADE, related_name="teams")
    pokemon = models.ManyToManyField(Pokemon, related_name = "teams", blank = True)

    def __str__(self):
        return self.name

def team_changed(sender, **kwargs):
    """
    This function will be listening to changes in the Many-to-Many relation of Team and Pokemon.
    If there are more than 6 pokemons in a team, a ValidationError will be raised
    """

    if kwargs["instance"].pokemon.count() > 6:
        raise ValidationError("You can't have more than 6 pokemon in a single team")

m2m_changed.connect(team_changed, sender = Team.pokemon.through)
