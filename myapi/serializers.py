from .models import Pokemon, Team, Trainer
from requests import get
from rest_framework import serializers

def get_pokemon_info(pokemon_name):
    info = get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}").json()
    return {"height": info["height"], "weight": info["weight"], "types": info["types"]}

"""
The following classes are used to serialize information.
This means the information from a model will be converted into a JSON format
"""
class PokemonSerializer(serializers.HyperlinkedModelSerializer):
    data = serializers.SerializerMethodField()
    class Meta:
        model = Pokemon
        fields = ['url', 'name', 'data']

    def get_data(self, obj):
        """
        The data of each pokemon isn't saved in our database, so we make an API call to retrieve it.
        """
        return get_pokemon_info(obj.name)

class TeamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Team
        fields = ["url", "name", "pokemon", "trainer"]

class TrainerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Trainer
        fields = ["url", "name", "teams"]

