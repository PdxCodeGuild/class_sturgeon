from rest_framework import generics, permissions, viewsets
from rest_framework import filters
from django.contrib.auth import get_user_model
from rest_framework.decorators import permission_classes

from pokemon import models
from .serializers import PokemonSerializer, UserSerializer
from .permissions import isStafforReadOnly

class PokemonViewSet(viewsets.ModelViewSet):
    queryset = models.Pokemon.objects.all()
    serializer_class = PokemonSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = [
        'number',
        'name',
        'height',
        'weight',
        'types__type',
        'caught_by__username',
        ]
    ordering_fields = '__all__'
    permission_classes = [isStafforReadOnly]

class CurrentPokemonView(generics.RetrieveAPIView):
    serializer_class = PokemonSerializer
    def get_object(self):
        return self.request.user

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    def get_object(self):
        return self.request.user



# class ListPokemon(generics.ListCreateAPIView):
#     queryset = models.Pokemon.objects.all()
#     serializer_class = PokemonSerializer
#     filter_backends = [filters.SearchFilter, filters.OrderingFilter]
#     search_fields = [
#         'number',
#         'name',
#         'height',
#         'weight',
#         'types__type',
#         'caught_by__username',
#         ]
#     ordering_fields = '__all__'
#     permission_classes = [isStafforReadOnly]

# class DetailPokemon(generics.RetrieveUpdateDestroyAPIView):
#     queryset = models.Pokemon.objects.all()
#     serializer_class = PokemonSerializer