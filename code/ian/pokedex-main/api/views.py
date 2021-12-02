from django.shortcuts import render
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import filters


from pokemon.models import Pokemon, Type
from users.models import CustomUser
from .serializers import PokemonSerializer, TypeSerializer, UserSerializer

# Create your views here.
class PokemonViewSet(viewsets.ModelViewSet):
    queryset = Pokemon.objects.all()
    serializer_class = PokemonSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['username']
   

class CurrentUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user


# class ListPokemon(generics.ListCreateAPIView):
#     queryset = models.Pokemon.objects.all()
#     serializer_class = PokemonSerializer

# class  DetailPokemon(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Pokemon.objects.all()
#     serializer_class = PokemonSerializer

class ListType(generics.ListCreateAPIView):
    queryset = Type.objects.all()
    serializer_class = TypeSerializer