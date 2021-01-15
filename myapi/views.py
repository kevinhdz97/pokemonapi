from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .serializers import PokemonSerializer, TeamSerializer, TrainerSerializer
from rest_framework.response import Response
from .models import Pokemon, Team, Trainer

# Views will be subclasses of ModelViewSet to be able to CRUD easily
class PokemonViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows POKEMON to be Created, Read, Updated or Deleted
    """
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer

class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows TEAMS to be Created, Read, Updated or Deleted
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows TRAINERS to be Created, Read, Updated or Deleted
    """
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer