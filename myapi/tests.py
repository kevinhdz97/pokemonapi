from django.test import TestCase, Client
from .models import Pokemon, Team, Trainer
from django.core.exceptions import ValidationError
import requests
from rest_framework.test import RequestsClient, APITestCase

class PokemonTestCase(TestCase):

    def setUp(self):
        """
        To create objects that will exist in every test case
        """

        # Creating pokemons
        pokemon1 = Pokemon.objects.create(name="charmander")
        pokemon2 = Pokemon.objects.create(name="blastoise")
        pokemon3 = Pokemon.objects.create(name="moltres")
        pokemon4 = Pokemon.objects.create(name="mewtwo")
        pokemon5 = Pokemon.objects.create(name="zapdos")
        pokemon6 = Pokemon.objects.create(name="dialga")
        pokemon7 = Pokemon.objects.create(name="arceus")

        # Creating trainers
        trainer1 = Trainer.objects.create(name="trainer1")

        # Creating teams
        team1 = Team.objects.create(name="team1", trainer = trainer1)

    def test_pokemon_limit(self):
        pokemon1 = Pokemon.objects.get(name="charmander")
        pokemon2 = Pokemon.objects.get(name="blastoise")
        pokemon3 = Pokemon.objects.get(name="moltres")
        pokemon4 = Pokemon.objects.get(name="mewtwo")
        pokemon5 = Pokemon.objects.get(name="zapdos")
        pokemon6 = Pokemon.objects.get(name="dialga")
        pokemon7 = Pokemon.objects.get(name="arceus")

        team1 = Team.objects.get(name="team1")

        # We add 6 pokemon first
        team1.pokemon.add(pokemon1)
        team1.pokemon.add(pokemon2)
        team1.pokemon.add(pokemon3)
        team1.pokemon.add(pokemon4)
        team1.pokemon.add(pokemon5)
        team1.pokemon.add(pokemon6)

        # We catch the validation error that will occur when adding a 7th pokemon
        with self.assertRaises(ValidationError):
            team1.pokemon.add(pokemon7)

    def test_request(self):
        """
        This is to simulate being a client and going to the tested url
        """
        c = Client() 
        response = c.get("/api/")

        # Test that the response status for the root of the api gets a correct response
        self.assertEqual(response.status_code, 200)

    def test_pokemon_number(self):
        """
        Testing that we get a count of 7 pokemon when we make an API call for the pokemon list
        """
        response = self.client.get("/api/pokemon", follow=True)
        self.assertEqual(response.data["count"], 7)

    def test_bad_request(self):
        """
        Testing what would happen if we search for a non-existent pokemon
        """
        response = self.client.get("/api/pokemon/100", follow=True)

        self.assertEqual(response.status_code, 404)