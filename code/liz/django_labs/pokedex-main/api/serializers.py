from rest_framework import serializers

from pokemon.models import Pokemon, Type
from users.models import CustomUser


class NestedPokemonSerializer (serializers.ModelSerializer):
    class Meta:
        fields = ('name', )
        model = Pokemon

class NestedTypeSerializer (serializers.ModelSerializer):
    class Meta:
        fields = ('type',)
        model = Type

class PokemonSerializer (serializers.ModelSerializer):
    type_info = NestedTypeSerializer(many=True, source='types')
    class Meta:
        fields = ('number', 'name', 'height', 'weight', 'image_front', 'image_back', 'caught_by', 'type_info', 'id')
        model = Pokemon

class TypeSerializer (serializers.ModelSerializer):
    pokemon_info = NestedPokemonSerializer(many=True, source='pokemon')
    class Meta:
        fields = ('type', 'pokemon_info')
        model = Type

class CustomUserSerializer (serializers.ModelSerializer):
    class Meta:
        fields = ('caught', 'id', 'username')
        model = CustomUser