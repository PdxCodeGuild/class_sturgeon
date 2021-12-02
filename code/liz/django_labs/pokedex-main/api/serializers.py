from rest_framework import serializers

from pokemon.models import Pokemon, Type



class NestedTypeSerializer (serializers.ModelSerializer):
    class Meta:
        fields = ('type',)
        model = Type

class PokemonSerializer (serializers.ModelSerializer):
    type_info = NestedTypeSerializer(many=True, source='types')
    class Meta:
        fields = ('number', 'name', 'height', 'weight', 'image_front', 'image_back', 'caught_by', 'type_info')
        model = Pokemon

class TypeSerializer (serializers.ModelSerializer):
    class Meta:
        fields = ('type', 'pokemon')
        model = Type