from django.shortcuts import render
from rest_framework import generics
from pokemon import models
from .serializers import pokemonSerializer,typeSerializer



class Listpokemon(generics.ListCreateAPIView):
    queryset = models.Pokemon.objects.all()
    serializer_class = pokemonSerializer
    filterset_fields = ['name', 'number']


class Detailpokemon(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Pokemon.objects.all()
    serializer_class = pokemonSerializer
    filterset_fields = ['type',]