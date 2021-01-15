from django.urls import path,include
from rest_framework import routers
from . import views

# Registering endpoints to get data from our models
router = routers.DefaultRouter()
router.register("pokemon", views.PokemonViewSet)
router.register("teams", views.TeamViewSet)
router.register("trainers", views.TrainerViewSet)

urlpatterns = [
    path("", include(router.urls))
]