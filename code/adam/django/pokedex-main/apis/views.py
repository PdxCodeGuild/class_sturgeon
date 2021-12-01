from rest_framework import generics
from rest_framework import filters

from pokemon import models
from .serializers import PokemonSerializer
from .permissions import isStafforReadOnly

class ListPokemon(generics.ListCreateAPIView):
    queryset = models.Pokemon.objects.all()
    serializer_class = PokemonSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        'firstName',
        'lastName',
        'cohort',
        'favoriteTopic',
        'favoriteTeacher',
        'capstone',
        ]
    ordering_fields = '__all__'
    permission_classes = [isStafforReadOnly]

class DetailPokemon(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Pokemon.objects.all()
    serializer_class = PokemonSerializer