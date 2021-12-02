from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import PokemonViewSet, TypeViewSet

router = DefaultRouter()
router.register('pokemon', PokemonViewSet, basename='pokemon')

urlpatterns = router.urls + [
    
]