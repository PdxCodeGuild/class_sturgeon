from django.urls import path

from .views import PokemonViewSet, CurrentPokemonView, CurrentUserView, UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('pokemon', PokemonViewSet, basename='pokemon')
router.register('users', UserViewSet, basename='users')

urlpatterns = router.urls + [
    path('currentuser/', CurrentUserView.as_view()),
    path('currentpokemon/', CurrentPokemonView.as_view())
]







# urlpatterns = [
#     path('', ListPokemon.as_view()),
#     path('<int:pk>/', DetailPokemon.as_view()),
# ]