from rest_framework import serializers
from pokemon import models


class NestedPokemonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'number',
            'name',
            'height',
            'weight',
            'image_front',
            'image_back',
            'caught_by',
            'types',
        )
        model = models.Pokemon

class PokemonSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'number',
            'name',
            'height',
            'weight',
            'image_front',
            'image_back',
            'caught_by',
            'types',
        )
        model = models.Pokemon